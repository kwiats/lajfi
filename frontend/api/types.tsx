export interface User {
  id: number;
  username: string;
  firstName: string;
  lastName: string;
  email: string;
}

export interface Task {
  id: number;
  user: User;
  title: string;
  description: string;
  priority: number;
  due_date: string; // lub Date, w zależności od formatu daty
  completed: boolean;
  created_at: string; // lub Date
  updated_at: string; // lub Date
}

export interface Event {
  id: number;
  user: User;
  title: string;
  description: string;
  start_time: string; // lub Date
  end_time: string; // lub Date
  created_at: string; // lub Date
  updated_at: string; // lub Date
}
