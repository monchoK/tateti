import 'package:flutter/material.dart';

import 'package:tateti_app/screens/mainscreens.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          primaryColor: Colors.deepPurple.shade100,
          canvasColor: null,
          secondaryHeaderColor: null,
          backgroundColor: Colors.deepPurple.shade400,
        ),
        home: MyHome());
  }
}
