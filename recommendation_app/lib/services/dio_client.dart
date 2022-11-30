import 'dart:convert';

import 'package:dio/dio.dart';

class DioClient {
  final Dio _dio;

  DioClient(this._dio) {
    _dio
      ..options.baseUrl = Endpoints.demoBaseUrl
      ..options.connectTimeout = Endpoints.connectionTimeout
      ..options.receiveTimeout = Endpoints.receiveTimeout
      ..options.responseType = ResponseType.json;
  }

  Future<Response> get({required String url}) async {
    // List<Map<String, dynamic>> responseJson;
    try {
      final response = await _dio.get<dynamic>(url);
      return response;
    } catch (e) {
      print(e.toString());
      rethrow;
    }
  }
}

class Endpoints {
  Endpoints._();

  static const String demoBaseUrl =
      "http://18.206.40.170:5000/api/v1/books_recommendation_for_user/";
  static const String baseUrl =
      "http://127.0.0.1:5000/api/v1/books_recommendation_for_user/";

  static const int connectionTimeout = 15000;

  static const int receiveTimeout = 15000;
}
