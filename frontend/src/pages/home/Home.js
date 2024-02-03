import React from 'react';
import Hero1 from './hero6.png';
import Hero5 from './hero5.png';
import Hero6 from './hero6.png';
import Hero7 from './hero7.png';
import { FaGithub } from 'react-icons/fa';

function Home() {
  const images = [Hero5, Hero6, Hero7, Hero1];
  const allImages = [...images, ...images];
  return (
    <div className="container mx-auto bg-gray-950 p-8 text-white">
      <div className="carousel-container">
        <h1 className="carousel-text">romarr</h1>
        <div className="carousel">
          {allImages.map((src, index) => (
            <img key={index} src={src} alt={`Carousel ${index}`} className="carousel-image" />
          ))}
        </div>
      </div>

      <div className="mb-8 text-lg leading-relaxed">
        <p className="mb-4 font-bold">
          Romarr is a web application designed to cater to gamers of all kinds. Just like Sonarr and Radarr are
          essential tools for managing your TV shows and movies, Romarr serves as your ultimate library organizer for
          video games. With Romarr, you can effortlessly track, manage, and discover new games while keeping your
          digital library in pristine order.
        </p>

        <h2 className="mb-4 text-3xl font-bold text-gray-300">Key features of Romarr:</h2>

        <p className="mb-4">
          <strong className="text-primary-light">Seamless Game Library Management:</strong> Romarr allows you to
          effortlessly import and organize your entire gaming collection. Whether you have games on Steam, Epic Games
          Store, PlayStation Network, Xbox Live, or any other platform, Romarr centralizes all your titles in one
          convenient location.
        </p>
        <p className="mb-4">
          <strong className="text-primary-light">Automated Game Downloads:</strong> Romarr automatically downloads games
          from your favorite indexers, and organizes them into your library. Romarr also automatically downloads
          metadata for your games, including cover art, descriptions, and more.
        </p>

        <h2 className="mb-4 text-3xl font-bold text-gray-300">How Romarr Makes Your Life Easier:</h2>
        <ul className="mb-8 list-inside list-disc pl-4 text-lg leading-relaxed">
          <li className="mb-4">
            Romarr automatically downloads games from your favorite indexers, and organizes them into your library.
          </li>
          <li className="mb-4">
            Romarr automatically downloads metadata for your games, including cover art, descriptions, and more.
          </li>
          <li className="mb-4">Romarr allows you to effortlessly import and organize your entire gaming collection.</li>
          <li className="mb-4">Romarr centralizes all your games in one convenient location.</li>
        </ul>

        <hr className="my-4 border-gray-700" />

        <footer className="mt-4 flex items-center justify-start rounded-xl bg-gray-900 p-5 shadow-lg">
          <a
            href="https://github.com/miikaoskari/romarr"
            className="mr-4 flex items-center rounded-3xl p-2 transition-all hover:bg-gray-700"
          >
            <FaGithub className="mr-2" />
            GitHub
          </a>
        </footer>
      </div>
    </div>
  );
}

export default Home;
