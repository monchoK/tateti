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
              cambiarvalor(valor);
            }));
  }

  void cambiarvalor(valor) {
    if (valor == "") {
      valor = "x";
    }
  }

  var valor = "";
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Theme.of(context).backgroundColor,
        body: Center(
          child: tablero(context, valor),
        ));
  }
}
