import 'package:flutter/material.dart';

class TatetiScreen extends StatefulWidget {
  const TatetiScreen({Key? key}) : super(key: key);

  @override
  State<TatetiScreen> createState() => _TatetiScreenState();
}

class _TatetiScreenState extends State<TatetiScreen> {
  Column tablero(BuildContext context, valor) {
    return Column(
      children: [
        cuerpo(context, valor),
        cuerpo(context, valor),
        cuerpo(context, valor)
      ],
    );
  }

  Column cuerpo(BuildContext context, valor) {
    return Column(children: [
      Row(
        children: [
          espacio(context, valor),
          espacio(context, valor),
          espacio(context, valor)
        ],
      )
    ]);
  }

  Container espacio(BuildContext context, valor) {
    return Container(
      color: Colors.grey.shade100,
      child: TextButton(
        child: Text(valor),
        onPressed: () {
          cambiar_valor(valor);
        },
      ),
    );
  }

  void cambiar_valor(valor) {
    if (valor == "") {
      valor = "x";
    }
  }

  @override
  var valor = "";
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Theme.of(context).backgroundColor,
        body: Center(
          child: tablero(context, valor),
        ));
  }
}
