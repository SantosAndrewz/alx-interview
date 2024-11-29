#!/usr/bin/node
/* A script too print all characters of Star Wars movie */

const request = require('request');

// Gets the movie ID from the command-line arguments
const movieID = process.argv[2];
// Construct a url
const movieURL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Retrieves the character's name from the URL
const getCharName = (charURL) => {
  return new Promise((resolve, reject) => {
    request(charURL, (error, response, body) => {
      if (error) return reject(error);
      resolve(JSON.parse(body).name);
    });
  });
};

// Function fetching movie data and then prints character names
request(movieURL, async (error, response, body) => {
  if (error) {
    console.error(`Error occured while fetching movie data: ${error}`);
    return;
  }

  try {
    const chars = JSON.parse(body).characters;
    for (const charURL of chars) {
      const charName = await getCharName(charURL);
      console.log(charName);
    }
  } catch (error) {
    console.error(`Error occured while processing character data: ${error}`);
  }
});
