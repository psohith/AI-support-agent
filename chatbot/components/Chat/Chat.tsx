import { FC, useEffect, useRef, useState } from "react";
import { ChatInput } from "./ChatInput";
import { ChatLoader } from "./ChatLoader";
import { ChatMessage } from "./ChatMessage";
import { IconRobot } from "@tabler/icons-react";

export const Chat: FC<Props> = ({ messages, loading, onSend, onReset }) => {
  const [isExpanded, setIsExpanded] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    if (messages.length > 0 && !isExpanded) {
      setIsExpanded(true);
    }
    scrollToBottom();
  }, [messages, loading]);

  return (
    <div
      className={`flex flex-col transition-all duration-500 ease-in-out ${
        isExpanded ? "h-[90vh]" : "h-[60px]"
      }`}
    >
      {/* Fixed Header */}
      <div className="flex-none z-10 backdrop-blur-sm bg-gradient-to-r from-cyan-500/90 to-blue-500/90 p-4 sm:p-6 shadow-lg">
        <div className="max-w-screen-xl mx-auto flex items-center justify-center gap-3">
          <IconRobot className="w-8 h-8 text-white animate-pulse" />
          <h1 className="font-sans text-2xl sm:text-3xl font-bold text-white tracking-tight">
            Eywa - AI Support Agent
          </h1>
        </div>
      </div>

      {/* Scrollable Messages Area */}
      <div
        className={`flex-1 overflow-y-auto px-2 sm:p-4 transition-all duration-500 ${
          isExpanded ? "opacity-100" : "opacity-0 h-0"
        }`}
      >
        {messages.map((message, index) => (
          <div key={index} className="my-1 sm:my-1.5">
            <ChatMessage message={message} />
          </div>
        ))}
        {loading && (
          <div className="my-1 sm:my-1.5">
            <ChatLoader />
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Fixed Chat Input */}
      <div className="flex-none p-2 bg-white border-t border-neutral-300">
        <ChatInput onSend={onSend} onReset={onReset} loading={loading} />
      </div>
    </div>
  );
};
