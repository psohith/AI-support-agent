import { Message } from "@/types";
import { IconArrowUp } from "@tabler/icons-react";
import { FC, KeyboardEvent, useEffect, useRef, useState } from "react";
import { ResetChat } from "./ResetChat";

interface Props {
  onSend: (message: Message) => void;
  onReset: () => void;
  loading?: boolean;
}

export const ChatInput: FC<Props> = ({ onSend, onReset, loading = false }) => {
  const [content, setContent] = useState<string>();

  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const handleChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    const value = e.target.value;
    if (value.length > 4000) {
      alert("Message limit is 4000 characters");
      return;
    }

    setContent(value);
  };

  const handleSend = () => {
    if (!content) {
      alert("Please enter a message");
      return;
    }
    onSend({ role: "user", content });
    setContent("");
  };

  const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  useEffect(() => {
    if (textareaRef && textareaRef.current) {
      textareaRef.current.style.height = "inherit";
      textareaRef.current.style.height = `${textareaRef.current?.scrollHeight}px`;
    }
  }, [content]);

  return (
    <div className="flex items-center gap-2 w-full">
      <div className="relative w-full">
        <textarea
          ref={textareaRef}
          className={`min-h-[44px] rounded-lg pl-4 pr-12 py-2 w-full focus:outline-none border-2 
          ${loading ? "bg-gray-100 " : "border-neutral-200"}
          transition-all duration-300 ease-in-out
          hover:border-transparent hover:ring-2 hover:ring-[#34d399]/50 hover:shadow-[0_0_15px_rgba(52,211,153,0.15)]
          focus:border-transparent focus:ring-2 focus:ring-gradient-to-r from-blue-500/90 to-cyan-500/90 focus:shadow-[0_0_20px_rgba(52,211,153,0.2)]
          bg-clip-padding`}
          style={{ resize: "none" }}
          placeholder={loading ? "Bot is thinking..." : "Type a message..."}
          value={content}
          rows={1}
          onChange={handleChange}
          onKeyDown={handleKeyDown}
        />

        <button
          onClick={() => handleSend()}
          disabled={loading}
          title="Send message"
        >
          <IconArrowUp
            className={`absolute right-2 bottom-3 h-8 w-8 hover:cursor-pointer rounded-full p-1 
            bg-gradient-to-r from-blue-500/90 to-cyan-500/90 
            text-white transition-all duration-300
            ${loading ? "opacity-50 cursor-not-allowed" : "hover:opacity-80"}`}
          />
        </button>
      </div>
      <ResetChat onReset={onReset} />
    </div>
  );
};
