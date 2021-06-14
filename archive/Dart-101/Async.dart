/* Sometimes its just worth waiting for ;) */
import 'dart:async';

const oneSecond = Duration(seconds: 1);

Future<void> afterASec(String msg) async {
  await Future.delayed(oneSecond);
  print(msg);
}

void main() {
  afterASec("Hi after 1 second");
}