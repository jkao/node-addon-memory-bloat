const bloat = require('bindings')('bloat');

class MyJSObject {
  constructor(value) {
    this.value_ = value;
  }
  value() {
    return this.value_;
  }
  plusOne() {
    this.value_ = this.value_ + 1;
    return this.value_;
  }
  multiply(other) {
    return new MyJSObject(this.value_ * other);
  }
}

let start;

console.log("node-addon-api version")
start = new Date();
for (let i = 0; i < 10000000; i++) {
  const x = new bloat.MyObject(1);
}
console.log(`Run time: ${new Date().getTime() - start.getTime()}`);

console.log("JS version")
start = new Date();

let x;
for (let i = 0; i < 10000000; i++) {
  x = new MyJSObject(parseInt(Math.random() * Math.floor(1000000)));
}
console.log(`Run time: ${new Date().getTime() - start.getTime()} ${x.value()}`);

// Some buffer time to capture memory usage
setTimeout(() => console.log("DONE"), 5000);
