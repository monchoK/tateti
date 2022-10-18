import 'package:flutter/material.dart';

import 'package:tateti_app/modelos/getUsers.dart';
import 'package:tateti_app/modelos/users.dart';

class GetUsers extends StatefulWidget {
  const GetUsers({Key? key}) : super(key: key);

  @override
  State<GetUsers> createState() => _GetUsersState();
}

class _GetUsersState extends State<GetUsers> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("USUARIOS")),
      body: FutureBuilder<Usuarios?>(
        future: ApisRequest().users,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator.adaptive());
          }
          final Usuarios? users = snapshot.data;
          return ListView.builder(
              itemCount: users?.usuarios.length ?? 0,
              itemBuilder: (context, index) {
                return ListTile(
                  title: Text(users!.usuarios[index].nombre),
                  subtitle: Text("Puntos: ${users.usuarios[index].puntos}"),
                );
              });
        },
      ),
    );
  }
}
