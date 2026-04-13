import FilmCard from "./FilmCard";
import { RiRobot3Line } from "@remixicon/react";

type Film = {
  title: string;
  rating: string;
  genre: string;
};

type ChatBubbleProps = {
  role: "bot" | "user";
  content: string;
  films?: Film[];
};

const feature = {
  icon: <RiRobot3Line className="text-4x" />,
};

export default function ChatBubble({ role, content, films }: ChatBubbleProps) {
  return (
    <div
      className={`flex ${role === "user" ? "justify-end" : "justify-start"} gap-3`}
    >
      {role === "bot" && (
        <div className="w-8 h-8 rounded-full bg-purple-600 flex items-center justify-center text-white text-xs shrink-0">
          <span className="text-white text-xs">{feature.icon}</span>
        </div>
      )}

      <div className="flex flex-col gap-3 max-w-sm">
        <div
          style={{
            padding: "12px 16px",
            fontSize: "14px",
            backgroundColor:
              role === "bot" ? "rgba(255,255,255,0.1)" : "#7c3aed",
            color: "white",
            borderRadius:
              role === "bot" ? "0px 16px 16px 16px" : "16px 0px 16px 16px",
          }}
        >
          {content}
        </div>

        {films && (
          <div className="grid grid-cols-3 gap-2">
            {films.map((film, i) => (
              <FilmCard key={i} {...film} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
