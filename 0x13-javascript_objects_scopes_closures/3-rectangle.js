#!/usr/bin/node
//class Rectangle that defines a rectangle
module.exports = class Rectangle{
    constructor(w, h) {
    		   if (h > 0 && w > 0) {
		   this.height = h;
		   this.width = w;
		   }
    }
    print() {
	for (let i = 0; i < this.height; i++) {
	    console.log('X'.repeat(this.width));
	}
    }
}
