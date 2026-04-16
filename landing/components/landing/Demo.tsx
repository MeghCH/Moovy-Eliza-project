"use client";

import { useState } from "react";
import { RiRobot3Line, RiPlayCircleLine, RiCloseLine } from "@remixicon/react";

const YOUTUBE_VIDEO_ID = "https://youtu.be/fnNiOG_aSVI";

export default function Demo() {
  const [modalOpen, setModalOpen] = useState(false);

  const films = [
    {
      title: "Scream",
      rating: "8.3",
      genre: "Horror",
      poster:
        "https://image.tmdb.org/t/p/w300//t/p/w600_and_h900_face/3O3klyyYpAZBBE4n7IngzTomRDp.jpg",
    },
    {
      title: "Rosemary's baby",
      rating: "8.1",
      genre: "Horror",
      poster:
        "https://image.tmdb.org/t/p/w300/t/p/w600_and_h900_face/8xreLDdWHQZa2u3zObRuOdNJDpm.jpg",
    },
    {
      title: "Shining",
      rating: "8.5",
      genre: "Thriller / Horror",
      poster:
        "https://image.tmdb.org/t/p/w300/t/p/w600_and_h900_face/fFYAlrOudDJRYs8tvuHbUk0OGdL.jpg",
    },
  ];
  const feature = {
    icon: <RiRobot3Line className="text-4x" />,
  };

  return (
    <section className="flex flex-col items-center py-24 px-4">
      <p className="text-gray-400 text-sm tracking-widest uppercase mb-8">
        Voir en action
      </p>

      <div className="w-full max-w-3xl bg-white/5 border border-white/10 rounded-2xl p-8 flex flex-col gap-6">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-full bg-purple-600 flex items-center justify-center shrink-0">
            <span className="text-white text-xs">{feature.icon}</span>
          </div>
          <div
            style={{
              padding: "8px 16px",
              fontSize: "14px",
              backgroundColor: "rgba(255,255,255,0.1)",
              color: "white",
              borderRadius: "0px 12px 12px 12px",
            }}
          >
            Un film pour frissonner un dimanche ?
          </div>
        </div>

        <div className="flex justify-end">
          <div
            style={{
              padding: "8px 24px",
              fontSize: "14px",
              backgroundColor: "#7c3aed",
              color: "white",
              borderRadius: "12px 0px 12px 12px",
            }}
          >
            Oui, un vieux film
          </div>
        </div>

        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-full bg-purple-600 flex items-center justify-center shrink-0">
            <span className="text-white text-xs">{feature.icon}</span>
          </div>
          <div
            style={{
              padding: "8px 16px",
              fontSize: "14px",
              backgroundColor: "rgba(255,255,255,0.1)",
              color: "white",
              borderRadius: "0px 12px 12px 12px",
            }}
          >
            Voici 3 films parfaits pour toi :
          </div>
        </div>

        <div className="grid grid-cols-3 gap-4 mt-2">
          {films.map((film, index) => (
            <div
              key={index}
              className="flex flex-col bg-white/5 border border-white/10 rounded-xl overflow-hidden"
            >
              <img
                src={film.poster}
                alt={film.title}
                className="w-full aspect-[2/3] object-contain"
              />
              <div className="p-3 flex flex-col gap-1">
                <p className="text-white text-sm font-medium">{film.title}</p>
                <p className="text-yellow-500 text-xs">★ {film.rating}</p>
                <span className="text-xs text-gray-400 bg-white/10 rounded-full px-2 py-0.5 w-fit">
                  {film.genre}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>

      <button
        onClick={() => setModalOpen(true)}
        className="relative mt-8 w-64 aspect-video rounded-xl overflow-hidden border border-white/10 group cursor-pointer"
      >
        <img
          src={`https://img.youtube.com/vi/${YOUTUBE_VIDEO_ID}/mqdefault.jpg`}
          alt="Aperçu vidéo démo"
          className="w-full h-full object-cover opacity-70 group-hover:opacity-50 transition-opacity"
        />
        <div className="absolute inset-0 flex flex-col items-center justify-center gap-1">
          <RiPlayCircleLine className="w-10 h-10 text-white group-hover:scale-110 transition-transform" />
          <span className="text-white text-xs font-medium">Voir la démo</span>
        </div>
      </button>

      {modalOpen && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm"
          onClick={() => setModalOpen(false)}
        >
          <div
            className="relative w-full max-w-3xl mx-4"
            onClick={(e) => e.stopPropagation()}
          >
            <button
              onClick={() => setModalOpen(false)}
              className="absolute -top-10 right-0 text-white/70 hover:text-white transition-colors"
            >
              <RiCloseLine className="w-7 h-7" />
            </button>
            <div className="relative w-full aspect-video rounded-2xl overflow-hidden border border-white/10">
              <iframe
                src={`https://www.youtube.com/embed/${YOUTUBE_VIDEO_ID}?autoplay=1&rel=0`}
                allow="autoplay; fullscreen; picture-in-picture"
                allowFullScreen
                className="absolute inset-0 w-full h-full"
              />
            </div>
          </div>
        </div>
      )}
    </section>
  );
}
