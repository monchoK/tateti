import 'dart:convert';

import 'package:tateti_app/modelos/users.dart';
import 'package:http/http.dart' as http;

class ApisRequest {
  Future<Usuarios?> get users async {
    var url = Uri.http("127.0.0.1:5000", "");
    final http.Response response = await http.get(url);

    if (response.statusCode == 200) {
      print(response.body);
      return usuariosFromJson(response.body);
    }
    return null;
  }
}
