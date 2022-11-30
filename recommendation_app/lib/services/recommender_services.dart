import 'package:dio/dio.dart';
import 'package:recommendation_app/models/user_model.dart';

import 'dio_client.dart';

class RecommenderServices {
  final DioClient dioClient;

  RecommenderServices({
    required this.dioClient,
  });

  Future<Response> getUser({required int id}) async {
    try {
      final response = dioClient.get(url: Endpoints.baseUrl);
      return response;
    } catch (e) {
      print(e.toString());
      rethrow;
    }
  }
}
