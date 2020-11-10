# forEach, Map and Filter

## printFirstAndLast

```
function printFirstAndLast(arr) {
    arr.forEach(function(str){
        console.log(str.charAt(0) + str.charAt(str.length - 1))
    })
}
```

## addKeyAndValue
```
function addKeyAndValue(arr, key, val) {
	arr.forEach(function(obj) {
		obj[key] = val
	})
	return arr
}
```

## valTimesIndex

```
function valTimesIndex(arr) {
	return arr.map(function(val, index, array) {
		return val * index
		})
}
```

## extractKey

```
function extractKey(arr, key) {
	return arr.map(function(val) {
		return val[key]
	})
}
```

## filterLetters

```
function filterLetters(arr, letter) {
    let count = 0
    let newArr = arr.filter(function(char) {
        return char === letter
    })
    return newArr.length
}
```

## filterKey

```
function filterKey(arr, key) {
	let newArr = arr.filter(function(obj) {
		return obj.hasOwnProperty(key)
	})
	return newArr
}
```

# Reduce

## extractKey

```
function extractKey(arr, key) {
    return arr.reduce(function(acc, next, index) {
        return acc.concat(next[key])
    }, [])
}
```

## filterLetters
```
function filterLetters(arr, letter) {
	return arr.reduce(function(acc, next) {
		if (letter === acc) {
			acc++
		}
		return acc
	}, 0)
}
```

## addKeyAndValue

```
function addKeyAndValue(arr, key, value) {
	return arr.reduce(function(acc, next) {
		next[key] = value
		return acc.concat(next)
	}, [])
}
```

# Iterators Exercises

# Part 1

```let users = [
  {
    username: 'larry',
    email: 'larry@foo.com',
    yearsExperience: 22.1,
    favoriteLanguages: ['Perl', 'Java', 'C++'],
    favoriteEditor: 'Vim',
    hobbies: ['Fishing', 'Sailing', 'Hiking'],
    hometown: {
      city: 'San Francisco',
      state: 'CA'
    }
  },
  {
    username: 'jane',
    email: 'jane@test.com',
    yearsExperience: 33.9,
    favoriteLanguages: ['Haskell', 'Clojure', 'PHP'],
    favoriteEditor: 'Emacs',
    hobbies: ['Swimming', 'Biking', 'Hiking'],
    hometown: {
      city: 'New York',
      state: 'NY'
    }
  },
  {
    username: 'sam',
    email: 'sam@test.com',
    yearsExperience: 8.2,
    favoriteLanguages: ['JavaScript', 'Ruby', 'Python', 'Go'],
    favoriteEditor: 'Atom',
    hobbies: ['Golf', 'Cooking', 'Archery'],
    hometown: {
      city: 'Fargo',
      state: 'SD'
    }
  },
  {
    username: 'anne',
    email: 'anne@test.com',
    yearsExperience: 4,
    favoriteLanguages: ['C#', 'C++', 'F#'],
    favoriteEditor: 'Visual Studio Code',
    hobbies: ['Tennis', 'Biking', 'Archery'],
    hometown: {
      city: 'Albany',
      state: 'NY'
    }
  },

  {
    username: 'david',
    email: 'david@test.com',
    yearsExperience: 12.5,
    favoriteLanguages: ['JavaScript', 'C#', 'Swift'],
    favoriteEditor: 'VS Code',
    hobbies: ['Volunteering', 'Biking', 'Coding'],
    hometown: {
      city: 'Los Angeles',
      state: 'CA'
    }
  }
];
```
## printEmails

```
function printEmails(arr) {
    return arr.reduce(function (acc, next) {
        return acc.concat(next['email'])
    },[])
}
```

## printHobbies

```
function printHobbies(arr) {
	return arr.reduce(function (acc, next) {
        return acc.concat(next['hobbies'])
    },[])
}
```

## findHometownByState

```
function findHometownByState(arr, str) {
	return arr.find(function(val) {
		return val.hometown.state === str
	})
}
```

## allLanguages

```
function allLanguages (arr) {
    let allLanguages = arr.reduce(function(acc, next) {
        return acc.concat(next['favoriteLanguages'])
    },[])

    return allLanguages.filter(function(val, index, array) {
        return array.indexOf(val) === index
    })
}
```

## hasFavoriteEditor

```
function hasFavoriteEditor(arr, str) {
	return arr.some(function(val) {
		return val.favoriteEditor === str
	})
}
```

## findByUsername

```
function findByUsername(arr, str) {
	return arr.find(function(val) {
		return val.username === str
	})
}
```


# Part 2

## vowelCount
```
function vowelCount(str) {
    let stringArray = str.split("")
    let vowels = ['a', 'e', 'i', 'o', 'u']
    return stringArray.reduce(function (acc, next) {
        if (vowels.includes(next.toLowerCase())) {
             if (next in acc) {
                acc[next]++
            } else {
                acc[next] = 1
            }
        }
        return acc
    }, {})
}
```

## removeVowels
```
function removeVowel(str) {
    let stringArray = str.split("")
    let vowels = ['a', 'e', 'i', 'o', 'u']
    return stringArray.reduce(function (acc, next) {
        if (!vowels.includes(next.toLowerCase()) {
             acc.push(next)
        }
        return acc
    }, [])
}

```

# Part 3

## listNames

```
function listNames(arr) {
	return arr.forEach(function(val) {
		console.log(val.name)
	})
}
```

## listSongDetails

```
function summerJamCount(arr) {
    return arr.filter(function (val) {
       return  val.month >= 6 && val.month < 9
    })
}
```

## summerJamCount

```
function summerJamCount(arr) {
    return arr.filter(function (val) {
       return  val.month >= 6 && val.month < 9
    })
}
```

## getDurations

```
function getDurations(arr) {
    return arr.filter(function (val) {
       return  val.duration
    })
}
```

## getDurationsInSeconds

```
function getDurationInSeconds(arr) {
    return arr.reduce(function (acc, song) {
        let time = song.duration.split(":")
        let mins = time[0]
        let seconds = time[1]
        let timeInSeconds = mins*60 +seconds
        
       return acc.concat(timeInSeconds)
    }, [])
}
```

## getMainArtists

```
function getMainArtists(arr) {
    return arr.map(function (song) {
        let mainArtist = song.artist
        if (song.artist.includes('featuring')) {
            mainArtist = mainArtist.split("featuring")[0]
        }
       return mainArtist
    })
}
```

## getBigHits

```
function getBigHits(arr) {
    return arr.filter(function (song) {
        
       return song.weeksAtNumberOne >= 10
    })
}
```

## getShortSongs

```
function getShortSongs(arr) {
    return arr.filter(function (song) {
        let songMins = song.duration.split(':')[0]
       return songMins < 3
    })
}
```

## getSongsByArtist

```
function getSongsByArtists(arr, artist) {
    return arr.filter(function (song) {
       return song.artist === artist
    })
}
```

## summerJamCount with reduce

```
function getSummerJamCount(arr, artist) {
    return arr.reduce(function (acc, song) {
        if(song.month >=6 && song.month < 9) {
            console.log(true)
            acc.push(song)
        }
       return acc
    }, [])
}
```

## getTotalDurationInSeconds

```
function getTotalDurationInSeconds(arr, artist) {
    let songsInSeconds = arr.reduce(function (acc, song) {
        let time = song.duration.split(":")
        let timeInSeconds = time[0]*60 + time[1]
        
       return acc.concat(parseInt(timeInSeconds))
    }, [])
    return songsInSeconds.reduce(function (acc, next) {
       return acc + next
    }, )
}
```

## getSongCountByArtist

```
function getSongCountByArtist(arr, artist) {
    return arr.reduce(function (acc, next) {
        if(acc[next.artist]) {
            acc[next.artist]++
        } else {
            acc[next.artist] = 1
        }
       return acc
    }, {})
}
```

## averageWeeksAtNumberOne

```
function averageWeeksAtNumberOne(arr) {
    let totalWeeks = arr.reduce(function (acc, next) {
       return acc + next.weeksAtNumberOne
    }, 0)
    return totalWeeks/arr.length
}
```