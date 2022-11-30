import 'package:flutter/material.dart';

class CustomField extends StatelessWidget {
  const CustomField({
    Key? key,
    required this.fieldName,
    required this.hintText,
    required this.textInputAction,
    required this.textInputType,
    this.visibility,
    this.obscureText = false,
    this.suffix = false,
  }) : super(key: key);

  final String fieldName, hintText;
  final TextInputAction textInputAction;
  final TextInputType textInputType;
  final bool obscureText, suffix;
  final VoidCallback? visibility;

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          fieldName,
          style: const TextStyle(
            fontSize: 16,
            color: Colors.blueGrey,
          ),
        ),
        const SizedBox(
          height: 4,
        ),
        TextFormField(
          textInputAction: textInputAction,
          keyboardType: textInputType,
          obscureText: obscureText,
          // validator: ,
          decoration: InputDecoration(
            suffixIcon: suffix
                ? IconButton(
                    icon: Icon(
                      obscureText ? Icons.visibility : Icons.visibility_off,
                    ),
                    onPressed: visibility,
                  )
                : null,
            hintText: hintText,
            enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(8),
              borderSide: const BorderSide(color: Colors.grey),
            ),
            focusedBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(8),
              borderSide: const BorderSide(color: Colors.grey),
            ),
          ),
        ),
        const SizedBox(
          height: 12,
        ),
      ],
    );
  }
}
