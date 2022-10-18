import 'dart:convert';

Usuarios usuariosFromJson(String str) => Usuarios.fromJson(json.decode(str));

String usuariosToJson(Usuarios data) => json.encode(data.toJson());

class Usuarios {
  Usuarios({
    required this.mensaje,
    required this.usuarios,
  });

  final String mensaje;
  final List<Usuario> usuarios;

  factory Usuarios.fromJson(Map<String, dynamic> json) => Usuarios(
        mensaje: json["mensaje"],
        usuarios: List<Usuario>.from(
            json["usuarios"].map((x) => Usuario.fromJson(x))),
      );

  Map<String, dynamic> toJson() => {
        "mensaje": mensaje,
        "usuarios": List<dynamic>.from(usuarios.map((x) => x.toJson())),
      };
}

class Usuario {
  Usuario({
    required this.id,
    required this.nombre,
    required this.puntos,
  });

  final int id;
  final String nombre;
  final int puntos;

  factory Usuario.fromJson(Map<String, dynamic> json) => Usuario(
        id: json["id"],
        nombre: json["nombre"],
        puntos: json["puntos"],
      );

  Map<String, dynamic> toJson() => {
        "id": id,
        "nombre": nombre,
        "puntos": puntos,
      };
}
