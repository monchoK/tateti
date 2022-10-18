import 'package:flutter/material.dart';
import 'package:tateti_app/screens/getUsersScreens.dart';

class MyHome extends StatelessWidget {
  const MyHome({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("TATETI APP")),
      body: Container(
        child: MaterialButton(
          onPressed: () {
            Navigator.push(context,
                MaterialPageRoute(builder: (context) => const GetUsers()));
          },
          child: Text("Usuarios"),
        ),
      ),
    );
  }
}
