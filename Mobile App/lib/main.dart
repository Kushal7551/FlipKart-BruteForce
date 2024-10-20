import 'dart:async';
import 'dart:io';
import 'package:camera/camera.dart';
// import 'package:firebase_core/firebase_core.dart';
// import 'package:firebase_storage/firebase_storage.dart';
import 'package:flutter/material.dart';
import 'package:path_provider/path_provider.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  // await Firebase.initializeApp();
  final cameras = await availableCameras();
  runApp(MyApp(cameras: cameras));
}

class MyApp extends StatelessWidget {
  final List<CameraDescription> cameras;
  
  MyApp({required this.cameras});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Camera App',
      home: CameraScreen(cameras: cameras),
    );
  }
}

class CameraScreen extends StatefulWidget {
  final List<CameraDescription> cameras;

  CameraScreen({required this.cameras});

  @override
  _CameraScreenState createState() => _CameraScreenState();
}

class _CameraScreenState extends State<CameraScreen> with SingleTickerProviderStateMixin {
  late CameraController _controller;
  bool _isRecording = false;
  Timer? _timer;
  late AnimationController _animationController;
  late Animation<double> _animation;

  @override
  void initState() {
    super.initState();
    _controller = CameraController(
      widget.cameras[0],
      ResolutionPreset.high,
    );
    _controller.initialize().then((_) {
      if (!mounted) return;
      setState(() {});
    });

    // Setup animation for recording indicator
    _animationController = AnimationController(
      vsync: this,
      duration: Duration(seconds: 1),
    )..repeat(reverse: true);  // Reverses the animation to create a blink effect

    _animation = CurvedAnimation(
      parent: _animationController,
      curve: Curves.easeInOut,
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    _timer?.cancel();
    _animationController.dispose();
    super.dispose();
  }

  void _startCapture() {
    setState(() {
      _isRecording = true;
    });

    // Start sending frames at regular intervals (e.g., every 2 seconds)
    _timer = Timer.periodic(Duration(seconds: 2), (timer) async {
      if (_isRecording) {
        await _captureFrame();
      } else {
        timer.cancel();
      }
    });
  }

  Future<void> _captureFrame() async {
    try {
      final image = await _controller.takePicture();

      // Save the image temporarily
      final directory = await getTemporaryDirectory();
      final imagePath = '${directory.path}/${DateTime.now().millisecondsSinceEpoch}.jpg';
      // await File(image.path).copy(imagePath);

      // Upload the image to Firebase
      // await _uploadToFirebase(File(imagePath));
    } catch (e) {
      print('Error capturing frame: $e');
    }
  }

  Future<void> _uploadToFirebase(File file) async {
    try {
      // final storageRef = FirebaseStorage.instance
          // .ref()
          // .child('frames/${DateTime.now().millisecondsSinceEpoch}.jpg');
      // await storageRef.putFile(file);
      print('Frame uploaded successfully');
    } catch (e) {
      print('Error uploading to Firebase: $e');
    }
  }

  void _stopCapture() {
    setState(() {
      _isRecording = false;
    });
    _timer?.cancel();
  }

  @override
  Widget build(BuildContext context) {
    if (!_controller.value.isInitialized) {
      return Center(child: CircularProgressIndicator());
    }

    return Scaffold(
      appBar: AppBar(title: Text('Camera Feed'),
      centerTitle: true,),
      body: Column(
        children: [
          Expanded(
            child: Center(
              child: AspectRatio(
                aspectRatio: 9.0/16.0,
                child: CameraPreview(_controller),
              ),
            ),
          ),
          if (_isRecording) _buildRecordingIndicator(),  // Display animation when recording
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: ElevatedButton(
              onPressed: _isRecording ? _stopCapture : _startCapture,
              child: Text(_isRecording ? 'Stop' : 'Start'),
            ),
          ),
        ],
      ),
    );
  }

  // Blinking recording indicator
  Widget _buildRecordingIndicator() {
    return Padding(
      padding: const EdgeInsets.only(bottom: 8.0),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          FadeTransition(
            opacity: _animation,
            child: Icon(
              Icons.fiber_manual_record,
              color: Colors.red,
              size: 30.0,
            ),
          ),
          SizedBox(width: 8),
          Text(
            'Recording...',
            style: TextStyle(color: Colors.red),
          ),
        ],
      ),
    );
  }
}
