function replaceWith(str, a, b) {
	let strArray = str.split("")
	
	for (let i=0; i<strArray.length;i++){
		if (strArray[i] == a){
			strArray[i] = b
		}
	}
	return strArray.join("")
}

function expand(arr, num) {
	let newArr = []
	for (let i=0;i<num;i++) {
		newArr.push(...arr)
	}
	
	return newArr
}

function acceptNumbersOnly(...args) {
	let argArr = args
	for(let i=0;i<argArr.length;i++) {
		if(isNaN(argArr[i]) || typeof(argArr[i]) !== 'number' ) {
			return false
		}
	}
	return true
}

function mergeArrays(arr1, arr2) {
	let newArr = arr1.concat(arr2)
	return newArr.sort()
}

function mergeObjects(obj1, obj2) {
	let finalObj = {}
	for (let property in obj1) {
		finalObj[property] = obj1[property]	}
	for (let property in obj2) {
	
	  finalObj[property] = obj2[property]
	}
	return finalObj
}


// Tests
describe("replaceWith", function() {
	it("replaces character", function() {
		expect(replaceWith('character', 'a', 'b')).toEqual('chbrbcter');
	})

	it("is case sensitive", function() {
		expect(replaceWith('atalitatical', 'a', 'b')).not.toEqual('BtBlitBticBl')	
	})
})

describe("expand", function () {
	it("expands array by supplied number", function() {
		expect(expand([2,3,4], 5)).toEqual([2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4])
	})
})

describe("acceptNumbersOnly", function() {
	it("returns false if NaN is included in arguments", function(){
		expect(acceptNumbersOnly(3, 3, NaN)).toBe(false)
	})

	it("returns false if string is included in arguments", function() {
		expect(acceptNumbersOnly(2, 4, 'be')).toBe(false)
	})
	it("returns true if all arguments are numbers", function() {
		expect(acceptNumbersOnly(3, 4, 5)).toBe(true)
	})
	it("returns false if any data types asides numbers are included in the argument", function() {
		expect(acceptNumbersOnly({}, [], undefined, null)).toBe(false)
	})
})

describe("mergeArrays", function() {
	it("should concatenate two arrays", function() {
		expect(mergeArrays([3,4,2], [1,7,5])).toEqual([1, 2, 3, 4, 5, 7])
	})
	it("Resultant array should not be unsorted", function() {
		expect(mergeArrays([3,4,2], [1,7,5])).not.toEqual([3, 4, 2, 1, 7, 5])
		expect(mergeArrays([3,4,2], [1,7,5])).toEqual([1, 2, 3, 4, 5, 7])
	})
})

describe("mergeObjects", function() {
	it("should combine two objects", function() {
		expect(
			mergeObjects({
				name: 'Foo'
				,num: 33
				,type: 'Food'
			}
			, {
				notation: 'JSON'
				,language: 'JavaScript'
				,artist: 'Falz'
			})).toEqual({
				name: 'Foo'
				,num: 33
				,type: 'Food'
				,notation: 'JSON'
				,language: 'JavaScript'
				,artist: 'Falz'
			})
		
	})
	it("If both objects contain same keys, the key value pair in the second object should override that of the first", function() {
		expect(
			mergeObjects({
				name: 'Foo'
				,num: 33
				,type: 'Food'
				,language: 'TypeScript'
			},
			 {
				test: 'thing'
				,language: 'JavaScript'
				,artist: 'Falz'
			})).toEqual({
				name: 'Foo'
				,num: 33
				,type: 'Food'
				,test: 'thing'
				,language: 'JavaScript'
				,artist: 'Falz'
			})
		
	})
})
