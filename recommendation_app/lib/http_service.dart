import 'package:recommendation_app/services/dio_client.dart';
import 'package:http/http.dart' as http;
import 'models/models.dart';

class HttpService {
  Future<UserModel> getData(String id) async {
    String url = '${Endpoints.demoBaseUrl}${int.parse(id)}';
    print(url);
    try {
      final response = await http.get(Uri.parse(url));
      if (response.statusCode == 200) {
        print(response.body);
        final user = UserModel.fromJson(response.body);
        return user;
      }
    } catch (e) {
      print(e.toString());
      throw e.toString();
    }
    return UserModel(
      id: '0',
      read: [],
      recommendation: [],
    );
  }

  // Future<void> getUser(String id) {
  //   String url = '${Endpoints.baseUrl}${int.parse(id)}';
  //   http
  //       .get(Uri.parse(url))
  //       .then((value) => print(value.body))
  //       .catchError((error) => print(error));
  // }
}
