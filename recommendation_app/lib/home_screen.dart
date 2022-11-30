import 'package:flutter/material.dart';
import 'package:recommendation_app/http_service.dart';

import 'login_screen.dart';

class HomeScreen extends StatelessWidget {
  HomeScreen({
    super.key,
    required this.userId,
  });

  final String userId;

  static const routeName = '/';

  static Route route({required String userId}) {
    return MaterialPageRoute(
      settings: const RouteSettings(name: routeName),
      builder: (_) => HomeScreen(
        userId: userId,
      ),
    );
  }

  final HttpService _httpService = HttpService();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        elevation: 0,
        automaticallyImplyLeading: false,
        title: const Text(
          'Book Recommendation',
          style: TextStyle(
            fontSize: 20,
            color: Colors.white,
          ),
        ),
        actions: [
          IconButton(
            onPressed: () => Navigator.pushReplacementNamed(
              context,
              LoginScreen.routeName,
            ),
            icon: const Icon(
              Icons.logout,
            ),
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'Books you have read',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.normal,
              ),
            ),
            Expanded(
              child: FutureBuilder(
                future: _httpService.getData(userId),
                builder: (context, snapshot) {
                  if (snapshot.hasData) {
                    final user = snapshot.data;
                    return ListView.builder(
                      itemCount: user!.read.length,
                      itemBuilder: (context, index) {
                        return ListTile(
                          contentPadding: const EdgeInsets.all(0),
                          title: Text(
                            user.read[index].Title,
                            style: const TextStyle(
                              fontSize: 16,
                            ),
                          ),
                          subtitle: Text(
                            user.read[index].Author,
                            style: const TextStyle(
                              fontSize: 14,
                            ),
                          ),
                        );
                      },
                    );
                  }
                  if (snapshot.hasError) {
                    return const Center(
                      child: Text('You have not read any books'),
                    );
                  }
                  return const LinearProgressIndicator();
                },
              ),
            ),
            Divider(
              height: 0,
              color: Colors.blueGrey,
            ),
            const SizedBox(
              height: 12,
            ),
            const Text(
              'Books you might like',
              style: TextStyle(
                fontSize: 16,
              ),
            ),
            Expanded(
              child: FutureBuilder(
                future: _httpService.getData(userId),
                builder: (context, snapshot) {
                  if (snapshot.hasData) {
                    final user = snapshot.data;
                    return ListView.builder(
                      itemCount: user!.recommendation.length,
                      itemBuilder: (context, index) {
                        return ListTile(
                          contentPadding: const EdgeInsets.all(0),
                          title: Text(
                            user.recommendation[index].Title,
                            style: const TextStyle(
                              fontSize: 16,
                            ),
                          ),
                          subtitle: Text(
                            user.recommendation[index].Author,
                            style: const TextStyle(
                              fontSize: 14,
                            ),
                          ),
                        );
                      },
                    );
                  }
                  if (snapshot.hasError) {
                    return const Center(
                      child: Text('Add books to get recommendations'),
                    );
                  }
                  return const LinearProgressIndicator();
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
