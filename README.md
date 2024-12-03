# Berkeley Pacman Project

Welcome to the repository for the **Berkeley Pacman Project**! This repository contains the implementation of **Project 1** and **Project 2** from the **CS188: Introduction to Artificial Intelligence** course at UC Berkeley. The project focuses on using artificial intelligence techniques to control Pacman and solve a variety of problems.

## Overview

In this repository, you will find the implementations of the following key projects:

- **Project 1**: **Search Algorithms** (Search for paths for Pacman using search techniques like Depth-First Search, Breadth-First Search, A* Search, and more).
- **Project 2**: **Multi-Agent Search and Reinforcement Learning** (Using search algorithms and reinforcement learning to control multiple agents like Pacman and ghosts).

The goal of the projects is to learn and apply various AI algorithms, including search, heuristic search, and reinforcement learning techniques, in a fun and engaging way using the Pacman environment.

## Table of Contents

1. [Project 1: Search](#project-1-search)
2. [Project 2: Multi-Agent Search & Reinforcement Learning](#project-2-multi-agent-search-reinforcement-learning)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Running the Tests](#running-the-tests)
6. [Credits](#credits)
7. [License](#license)

## Project 1: Search

In **Project 1**, the goal was to implement search algorithms that help Pacman find the optimal path through a maze. The project includes the following algorithms:

- **Depth-First Search (DFS)**
- **Breadth-First Search (BFS)**
- **A* Search**

These algorithms were implemented to explore the maze and find the best path from Pacman's starting point to a target (such as food pellets). Each algorithm has its own strengths and trade-offs, and we tested them on different mazes to evaluate their performance.

### Key Features

- **DFS**: Explores as deep as possible before backtracking.
- **BFS**: Finds the shortest path by exploring all possible nodes level by level.
- **A\* Search**: Uses heuristics to guide Pacman towards the goal more efficiently than BFS.

## Project 2: Multi-Agent Search & Reinforcement Learning

In **Project 2**, the goal was to extend the search algorithms to multi-agent scenarios and implement reinforcement learning algorithms for Pacman.

### Multi-Agent Search

Pacman now needs to plan moves while considering the behavior of the ghosts. We used **Minimax Search** and **Alpha-Beta Pruning** to determine Pacman's best moves while avoiding ghosts.

### Key Features

- **Multi-Agent Search**: Pacman must consider both the environment and ghost positions to make optimal decisions.

## Installation

To get started with the Pacman project, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/berkeley-pacman-project.git
   cd berkeley-pacman-project
