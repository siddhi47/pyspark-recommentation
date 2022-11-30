import 'package:flutter/material.dart';
import 'package:recommendation_app/models/models.dart';

import '../home_screen.dart';
import '../login_screen.dart';

class AppRouter {
  static Route onGenerateRoute(RouteSettings settings) {
    print('This is route: ${settings.name}');

    switch (settings.name) {
      case HomeScreen.routeName:
        return HomeScreen.route(
          userId: settings.arguments as String,
        );
      // userModel: settings.arguments as Future<UserModel>);

      case LoginScreen.routeName:
        return LoginScreen.route();

      default:
        return _errorRoute();
    }
  }

  static Route _errorRoute() {
    return MaterialPageRoute(
      settings: const RouteSettings(name: '/error'),
      builder: (_) => const Scaffold(
        body: Center(
          child: Text(
            'Error',
          ),
        ),
      ),
    );
  }
}
