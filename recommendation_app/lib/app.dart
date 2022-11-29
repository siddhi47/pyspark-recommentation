import 'package:flutter/material.dart';
import 'package:recommendation_app/config/app_router.dart';

import 'home_screen.dart';
import 'login_screen.dart';

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Book Recommendation',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(),
      initialRoute: LoginScreen.routeName,
      onGenerateRoute: AppRouter.onGenerateRoute,
    );
  }
}
