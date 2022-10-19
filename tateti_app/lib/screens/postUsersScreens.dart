import 'package:flutter/material.dart';
import 'package:tateti_app/modelos/users.dart';

class PostUsers extends StatefulWidget {
  const PostUsers({Key? key}) : super(key: key);

  @override
  State<PostUsers> createState() => _PostUsersState();
}

class _PostUsersState extends State<PostUsers> {
  final nombre = TextEditingController();
  final url = Uri.parse("http://127.0.0.1:5000/usuarios");
  final headers = {"Content-Type": "application/json;charset=UTF-8"};

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Theme.of(context).backgroundColor,
        appBar: AppBar(title: const Text("Agregar Usuario")),
        body: Column(children: [
          Container(
              color: Theme.of(context).primaryColor,
              child: const Text(
                "Registre su usuario",
              )),
          Container(
              decoration: BoxDecoration(
                  color: Colors.white, borderRadius: BorderRadius.circular(10)),
              margin: const EdgeInsets.all(10),
              padding: const EdgeInsets.all(10),
              child: TextField(
                controller: nombre,
                decoration: const InputDecoration(
                    hintText: "Nombre", border: InputBorder.none),
              )),
          Container(
              color: Theme.of(context).primaryColor,
              child: const MaterialButton(
                onPressed: null,
                child: Text("Crear usuario"),
              )),
        ]));
  }
}
