import React, { useEffect, useState } from 'react';
import styles from './styles.module.css';

const quotes = [
  {
    text: "Your mental health is a priority. Your happiness is essential. Your self-care is a necessity.",
    author: "-----"
  },
  {
    text: "You don't have to control your thoughts. You just have to stop letting them control you.",
    author: "Dan Millman"
  },
  {
    text: "Recovery is not one and done. It is a lifelong journey that takes place one day, one step at a time.",
    author: "-----"
  },
  {
    text: "Mental health problems don't define who you are. They are something you experience.",
    author: "Mental Health Foundation"
  },
  {
    text: "You are not alone. You are seen. You are heard. You are loved.",
    author: "-----"
  },
  {
    text: "It's okay to not be okay – it means that your mind is trying to heal itself.",
    author: "Jasmine Warga"
  },
  {
    text: "Self-care is not selfish. You cannot serve from an empty vessel.",
    author: "Eleanor Brown"
  },
  {
    text: "Your present circumstances don't determine where you can go; they merely determine where you start.",
    author: "Nido Qubein"
  },
  {
    text: "You are stronger than you know, braver than you believe, and smarter than you think.",
    author: "Christopher Robin"
  },
  {
    text: "The strongest people are those who win battles we know nothing about.",
    author: "-----"
  }
];

const Login = () => {
  const [currentQuotes, setCurrentQuotes] = useState([]);

  useEffect(() => {
    updateQuotes();
    const interval = setInterval(updateQuotes, 10000);
    return () => clearInterval(interval);
  }, []);

  const googleAuth = () => {
	window.open(
		`${process.env.REACT_APP_API_URL}/auth/google/callback`,
		"_self"
	);
	};

  const getRandomQuote = (excludeQuotes = []) => {
    const availableQuotes = quotes.filter(
      (quote) => !excludeQuotes.some((eq) => eq.text === quote.text)
    );
    return availableQuotes[Math.floor(Math.random() * availableQuotes.length)];
  };

  const updateQuotes = () => {
    const newQuotes = Array(3)
      .fill(null)
      .map(() => getRandomQuote(currentQuotes));
    setCurrentQuotes(newQuotes);
  };

  return (
    <div className={styles.container}>
      <div className={styles.logoContainer}>
        <img
          src="./images/Logo1.png"
          alt="Logo"
          className={styles.logo}
        />
      </div>
      <button className={styles.loginButton} >Login</button>
      <div className={styles.welcomeText}>
        <h1>Welcome</h1>
        <p>Let's fight the battles together</p>
      </div>
      <div className={styles.flashCardsContainer}>
        {currentQuotes.map((quote, index) => (
          <div key={index} className={styles.flashCard}>
            <p className={styles.quote}>{quote.text}</p>
            <span className={styles.author}>- {quote.author}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Login;
