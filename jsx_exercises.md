# Part 1

## FirstComponent

```
class FirstComponent extends React.Component {
	render() {
		return (
			<div>
				<h1>My very first component.</h1>
			</div
		);	
	}
}
ReactDOM.render(<FirstComponent />, document.getElementById('app'))
```
## SecondComponent

```
class SecondComponent extends React.Component {
	render() {
		return (
			<div>
				<h1>My very first component.</h1>
			</div
		);	
	}
}
ReactDOM.render(<SecondComponent />, document.getElementById('app'))
```

## NamedComponent 

```
class NamedComponent extends React.Component {
	render() {
		return (
			<div>
				<h1>My name is {this.props.name}.</h1>
			</div
		);	
	}
}
ReactDOM.render(<NamedComponent name="Ade" />, document.getElementById('app'))
```

# Part 2

```
class Tweet extends React.Component {
	render() {
		return (
			<div>
				<div>
					<div className="user">
						<h6>{this.props.name}</h6>
						<h1>@{this.props.username}.</h1>
					</div>
					<div className="date">
						<h1>My name is {this.props.date}.</h1>
					</div>
				</div>
				<div className="mesage">
					<h1>My name is {this.props.message}.</h1>
				</div
			</div
		);	
	}
}

class App extends React.Component {
	render() {
		return (
			<Tweet username="" name="" date="" message="" />
			<Tweet username="" name="" date="" message="" />
			<Tweet username="" name="" date="" message="" />
		);	
	}
}
ReactDOM.render(<App />, document.getElementById('app'))
```

# Part 3

```
class Person extends React.Component {
  render() {
    let age = this.props.age;
    let name = this.props.name
    let message = ''
    if (name >= 21) {
      message = 'Have a drink!';
    } else {
      message = 'You must be 21';
    }
    if(name.length > 8) {
    	name = name.slice(0,6)
    }
    return (
      <div>
        <p>Learn some information about this person</p>
        <h3>{message}</h3>
        <p>{name}</p>
        <ul>
          {this.props.hobbies.map(listitem => (
            <li key={listitem}>
              {listitem}
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

class App extends React.Component {
	render() {
		return (
			<Person name="" age=23 hobbies=[] />
			<Person name="" age=23 hobbies=[] />
			<Person  name="" age=23 hobbies=[]  />
		);	
	}
}
ReactDOM.render(<App />, document.getElementById('app'))
```