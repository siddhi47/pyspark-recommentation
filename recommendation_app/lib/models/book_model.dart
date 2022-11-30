import 'dart:convert';

class BookModel {
  final String Title;
  final String Author;
  BookModel({
    required this.Title,
    required this.Author,
  });

  BookModel copyWith({
    String? Title,
    String? Author,
  }) {
    return BookModel(
      Title: Title ?? this.Title,
      Author: Author ?? this.Author,
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'Title': Title,
      'Author': Author,
    };
  }

  factory BookModel.fromMap(Map<String, dynamic> map) {
    return BookModel(
      Title: map['Title'] ?? '',
      Author: map['Author'] ?? '',
    );
  }

  String toJson() => json.encode(toMap());

  factory BookModel.fromJson(String source) =>
      BookModel.fromMap(json.decode(source));

  @override
  String toString() => 'BookModel(Title: $Title, Author: $Author)';

  @override
  bool operator ==(Object other) {
    if (identical(this, other)) return true;

    return other is BookModel && other.Title == Title && other.Author == Author;
  }

  @override
  int get hashCode => Title.hashCode ^ Author.hashCode;
}
