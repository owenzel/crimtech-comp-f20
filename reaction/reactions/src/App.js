import logo from './logo.svg';
import './App.css';
import React from 'react';

class Panel extends React.Component {
  constructor(props) {
    super(props);
    this.state = { start_time: 0, ran_once: false, counting: false, true_duration: 0, reaction_time: 0, color: 'green'};
    this.process_click = this.process_click.bind(this);
  }
  handle_color = (c) => {
    this.setState({color: c})
  }
  start_count() {
    this.setState({start_time:window.performance.now()}) //how many milliseconds it has been since the website has loaded
    this.setState({true_duration:(Math.floor(Math.random() * 6) + 2) * 1000})
    this.setState({counting:true})
    this.handle_color('darkred')
    setTimeout(this.handle_color, 3000, 'green');
  }
  end_count() {
    if (window.performance.now() - this.state.start_time > this.state.true_duration)
    {
      this.setState({ran_once:true})
      this.setState({counting:false})
      this.setState({reaction_time:(window.performance.now() - this.state.true_duration - this.state.start_time)})
    }
  }
  process_click() {
    if (this.state.counting) {
      this.end_count();
    } else this.start_count();
  }
  render() {
    let msg = "Click me to begin";
    if (this.state.counting && this.state.color === 'darkred')
    {
      msg = "Wait for Green"
    }
    else if (this.state.counting && this.state.color === 'green')
    {
      msg = "Click"
    }
    else if (this.state.ran_once)
    {
      msg = `Your reaction time is ${this.state.reaction_time} ms`
    }
    return (
      <div className = "PanelContainer" onClick = {this.process_click} style={ { background: this.state.color} }>
        <div className = "Panel">{msg}</div>
      </div>
    );
  }
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1 className =  "Header">How Fast is your Reaction Time?</h1>
        <Panel />
        <p>Click as soon as the red box turns green. Click anywhere in the box to start.</p>
      </header>
    </div>
  );
}

export default App;
