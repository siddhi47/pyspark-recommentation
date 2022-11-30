// import 'package:dio/dio.dart';
// import 'package:recommendation_app/services/recommender_services.dart';

// import '../models/models.dart';

// class Repository {
//   final RecommenderServices recommenderServices;

//   Repository(this.recommenderServices);

//   Future<UserModel> getData(String id) async {
//     try {
//       final response = await recommenderServices.getUser(id: int.parse(id));
//       final user = response.data
//     } on DioError catch (e) {
//       throw e.message;
//     }
//   }
// }
