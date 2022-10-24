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
              child:
              cambiarvalor(valor);
            }));
  }

  Future<void> cambiarvalor(valor) async {
    if (valor == "") {
      valor = "x";
    }
    return valor;
  }

  var valor = "";
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Theme.of(context).backgroundColor,
        body: Container(
          padding: EdgeInsets.all(50),
          child: tablero(context, valor),
        ));
  }
}
