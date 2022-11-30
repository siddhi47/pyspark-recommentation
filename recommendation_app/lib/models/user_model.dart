import 'dart:convert';

import 'package:flutter/foundation.dart';

import 'package:recommendation_app/models/book_model.dart';

class UserModel {
  final String id;
  final List<BookModel> read;
  final List<BookModel> recommendation;
  UserModel({
    required this.id,
    required this.read,
    required this.recommendation,
  });

  UserModel copyWith({
    String? id,
    List<BookModel>? read,
    List<BookModel>? recommendation,
  }) {
    return UserModel(
      id: id ?? this.id,
      read: read ?? this.read,
      recommendation: recommendation ?? this.recommendation,
    );
  }

  Map<String, dynamic> toMap() {
    return <String, dynamic>{
      'id': id,
      'read': read.map((x) => x.toMap()).toList(),
      'recommendation': recommendation.map((x) => x.toMap()).toList(),
    };
  }

  factory UserModel.fromMap(Map<String, dynamic> map) {
    return UserModel(
      id: map['id'] ?? '',
      read: List<BookModel>.from(map['read']?.map((x) => BookModel.fromMap(x))),
      recommendation: List<BookModel>.from(
          map['recommendation']?.map((x) => BookModel.fromMap(x))),
    );
  }

  String toJson() => json.encode(toMap());

  factory UserModel.fromJson(String source) =>
      UserModel.fromMap(json.decode(source));

  @override
  String toString() =>
      'UserModel(id: $id, read: $read, recommendation: $recommendation)';

  @override
  bool operator ==(Object other) {
    if (identical(this, other)) return true;

    return other is UserModel &&
        other.id == id &&
        listEquals(other.read, read) &&
        listEquals(other.recommendation, recommendation);
  }

  @override
  int get hashCode => id.hashCode ^ read.hashCode ^ recommendation.hashCode;
}
