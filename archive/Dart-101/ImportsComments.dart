/*You gotta express 
  yourself more ;) */

import 'dart:io';
import 'package:lib1/lib1.dart';
//If 2 libraries have conflicting identifiers
import 'package:lib2/lib2.dart' as lib2;

/// Learning new things
/// Dont forget to say [sayHi]
void main() {
  // Uses Element from lib1.
  Element element1 = Element();

  // Uses Element from lib2.
  lib2.Element element2 = lib2.Element();

  void sayHi() => print("Hi");
  sayHi();
}
