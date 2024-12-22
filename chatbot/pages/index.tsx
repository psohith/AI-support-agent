import { Chat } from "@/components/Chat/Chat";
import { Footer } from "@/components/Layout/Footer";
import { Navbar } from "@/components/Layout/Navbar";
import { Message } from "@/types";
import Head from "next/head";
import { useEffect, useRef, useState } from "react";

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [currentChatCount, setCurrentChatCount] = useState<number>(0);

  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  const generateSessionId = () => {
    return Math.random().toString(36).substring(2, 15);
  };

  const handleSend = async (message: Message) => {
    let updatedMessages = [...messages, message];
    const sessionId = localStorage.getItem("session_id") || generateSessionId();

    if (!localStorage.getItem("session_id")) {
      setCurrentChatCount(0);
      localStorage.setItem("session_id", sessionId);
    }
    setCurrentChatCount(currentChatCount + 1);
    setMessages(updatedMessages);
    setLoading(true);

    try {
      const response = await fetch("http://localhost:5000/api/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: message.content,
          session_id: localStorage.getItem("session_id"),
        }),
      });

      if (!response.ok) {
        setLoading(false);
        throw new Error(`Error: ${response.status}`);
      }

      const data = await response.json();
      console.log(data);

      setMessages((messages) => [
        ...messages,
        {
          role: "assistant",
          content: data.response,
        },
      ]);
      if (currentChatCount === 8) {
        setCurrentChatCount(0);
        localStorage.setItem("session_id", generateSessionId());
        alert("Chat session has been reset due to max Limit constrain.");
      }
    } catch (error) {
      console.error("Error while fetching from API:", error);
      setMessages((messages) => [
        ...messages,
        {
          role: "assistant",
          content: "Oops! Something went wrong. Please try again later.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    const newSessionId = generateSessionId();
    localStorage.setItem("session_id", newSessionId);

    setMessages([
      {
        role: "assistant",
        content: `Hi there! I'm Testsigma's Support Bot, your AI-powered assistant. I’m here to help you with your queries, resolve doubts, and provide guidance related to Testsigma. How can I assist you today?`,
      },
    ]);
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    setMessages([
      {
        role: "assistant",
        content: `Hi there! I'm Testsigma's Support Bot, your AI-powered assistant. I’m here to help you with your queries, resolve doubts, and provide guidance related to Testsigma. How can I assist you today?`,
      },
    ]);
  }, []);

  return (
    <>
      <Head>
        <title>Chatbot UI</title>
        <meta
          name="description"
          content="A simple chatbot starter kit for OpenAI's chat model using Next.js, TypeScript, and Tailwind CSS."
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/testsigma_logo.jpeg" />
      </Head>

      <div className="flex flex-col h-screen">
        <Navbar />

        <div className="flex-1 flex justify-center items-center">
          <div className="max-w-[800px] w-full max-h-[90vh] overflow-auto bg-white rounded shadow">
            <Chat
              messages={messages}
              loading={loading}
              onSend={handleSend}
              onReset={handleReset}
            />
            <div ref={messagesEndRef} />
          </div>
        </div>
        <Footer />
      </div>
    </>
  );
}
