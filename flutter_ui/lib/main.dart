import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(const CourseSaverApp());
}

class CourseSaverApp extends StatelessWidget {
  const CourseSaverApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'CourseSaver AI',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
        useMaterial3: true,
      ),
      home: const CourseSaverHomePage(),
    );
  }
}

class CourseSaverHomePage extends StatefulWidget {
  const CourseSaverHomePage({super.key});

  @override
  State<CourseSaverHomePage> createState() => _CourseSaverHomePageState();
}

class _CourseSaverHomePageState extends State<CourseSaverHomePage> {
  final TextEditingController timeController = TextEditingController();
  final TextEditingController videoController = TextEditingController();
  final TextEditingController scoreController = TextEditingController();

  String prediction = "";

  Future<void> getPrediction() async {
    final double timeSpent = double.tryParse(timeController.text) ?? 0;
    final int videosWatched = int.tryParse(videoController.text) ?? 0;
    final double quizScore = double.tryParse(scoreController.text) ?? 0;

    final response = await http.post(
      Uri.parse(
        'http://10.0.2.2:5000/predict',
      ), // for Android emulator use 10.0.2.2
      headers: {"Content-Type": "application/json"},
      body: json.encode({
        "time_spent": timeSpent,
        "videos_watched": videosWatched,
        "quiz_score": quizScore,
      }),
    );

    if (response.statusCode == 200) {
      final data = json.decode(response.body);
      setState(() {
        prediction = data['prediction'];
      });
    } else {
      setState(() {
        prediction = "Error: Server not responding.";
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("CourseSaver AI")),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          children: [
            TextField(
              controller: timeController,
              keyboardType: TextInputType.number,
              decoration: const InputDecoration(
                labelText: "Time Spent on Website (hrs)",
              ),
            ),
            const SizedBox(height: 12),
            TextField(
              controller: videoController,
              keyboardType: TextInputType.number,
              decoration: const InputDecoration(labelText: "Videos Watched"),
            ),
            const SizedBox(height: 12),
            TextField(
              controller: scoreController,
              keyboardType: TextInputType.number,
              decoration: const InputDecoration(labelText: "Quiz/Test Score"),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: getPrediction,
              child: const Text("Predict"),
            ),
            const SizedBox(height: 30),
            if (prediction.isNotEmpty)
              Card(
                color: Colors.grey.shade200,
                child: Padding(
                  padding: const EdgeInsets.all(16),
                  child: Text(
                    "Prediction: $prediction",
                    style: const TextStyle(fontSize: 18),
                  ),
                ),
              ),
          ],
        ),
      ),
    );
  }
}
