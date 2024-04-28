import axios from 'axios';
import './chatbot.css'
import { FaUser, FaRobot } from 'react-icons/fa';
import React, { useState, useEffect } from 'react'


const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [inputText, setInputText] = useState('');

  useEffect(() => {
    // Function to fetch initial messages or any other initialization
    fetchInitialMessages();
  }, []);

  const fetchInitialMessages = async () => {
    try {
      // Fetch initial messages from the backend when component mounts
      const response = await axios.get('http://localhost:5000/chat');
      setMessages([...messages, { text: response.data.response, sender: 'bot' }]);
      console.log(response.data.response);
      ; // Assuming messages are returned as an array
    } catch (error) {
      console.error('Error fetching initial messages:', error);
    }
  };

  const sendMessage = async () => {
    if (inputText.trim() === '') return;

    // Add the user's message to the chat interface
    setMessages(prevMessages => [...prevMessages, { text: inputText, sender: 'user' }]);
    setInputText('');

    try {
      // Send the user's message to the backend
      const response = await axios.post('http://localhost:5000/chat', {
        text: inputText,
      });
      console.log(messages);
      
      // Add the bot's response to the chat interface
      setMessages(prevMessages => [...prevMessages, { text: response.data.response, sender: 'bot' }]);
      // setMessages([...messages, { text: response.data.response, sender: 'bot' }]);
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  const handleInputChange = (e) => {
    setInputText(e.target.value);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      sendMessage();
    }
  };

  return (
<div className='body'>
    <div className='left'>
        <div className='bus-logo'></div>
        <h1>PaaruKutty</h1>
        <h2> Tours & Travels</h2>
    </div>       
    <div className="chatbot-container">
    <h1>Chatbot</h1>
    {/* <div className='chatbot-messages-container'> */}
      <div className="chatbot-messages">
        
      <div className="chatbot-background"></div>
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.sender}`}>
          {message.sender === 'user' ? <FaUser className="user-icon"  /> : <FaRobot className="bot-icon" />}
          <p style={{color:message.sender === 'user' ? 'white':'black'}}>{'        ' + message.text} </p>
          </div>
        ))}
      </div>
      <div className="chatbot-input">
        <input
          type="text"
          placeholder="Type a message..."
          value={inputText}
          onChange={handleInputChange}
          onKeyPress={handleKeyPress}
          
        />
        <button onClick={sendMessage}>Send</button>
      </div>
      </div>
    </div>
    //  </div>
   
  );
};

export default Chatbot;