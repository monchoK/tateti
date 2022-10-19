import 'package:flutter/material.dart';
import 'package:tateti_app/juego/tatetiScreen.dart';
import 'package:tateti_app/screens/getUsersScreens.dart';
import 'package:tateti_app/screens/postUsersScreens.dart';

class MyHome extends StatelessWidget {
  const MyHome({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Theme.of(context).backgroundColor,
      appBar: AppBar(title: const Text("TATETI APP")),
      body: Center(
        child: Row(mainAxisAlignment: MainAxisAlignment.spaceAround, children: [
          MaterialButton(
            color: Theme.of(context).primaryColor,
            onPressed: () {
              Navigator.push(context,
                  MaterialPageRoute(builder: (context) => const GetUsers()));
            },
            child: const Text("Ver Usuarios"),
          ),
          MaterialButton(
            color: Theme.of(context).primaryColor,
            onPressed: () {
              Navigator.push(context,
                  MaterialPageRoute(builder: (context) => const PostUsers()));
            },
            child: const Text("Registrar Usuario"),
          ),
          MaterialButton(
            color: Theme.of(context).primaryColor,
            onPressed: () {
              Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (context) => const TatetiScreen()));
            },
            child: const Text("Tateti"),
          )
        ]),
      ),
    );
  }
}
