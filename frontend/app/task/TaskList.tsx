import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, Button, StyleSheet } from 'react-native';
import { Task } from '../../api/types';
import { getTasks, createTask } from '../../api/common/services/TaskService';

const TaskList: React.FC = () => {
  const [tasks, setTasks] = useState<Task[]>([]);

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      const data = await getTasks();
      setTasks(data);
    } catch (error) {
      console.error('Error fetching tasks', error);
    }
  };

  const handleCreateTask = async () => {
    try {
      const newTask = {
        title: 'New Task',
        description: 'Description for new task',
        priority: 1,
        due_date: '2024-12-31T23:59:59',
        completed: false,
      };
      await createTask(newTask);
      fetchTasks(); // Refresh the task list
    } catch (error) {
      console.error('Error creating task', error);
    }
  };

  return (
    <View style={styles.container}>
      <Button title="Add Task" onPress={handleCreateTask} />
      <FlatList
        data={tasks}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View style={styles.taskItem}>
            <Text style={styles.title}>{item.title}</Text>
            <Text>{item.description}</Text>
          </View>
        )}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  taskItem: {
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
  },
});

export default TaskList;
