import { describe, expect, it } from 'vitest';
import { CreateUserUseCase } from '../../application/user/create-user.usecase.js';
import { IUserRepository, User } from './user.js';

class InMemoryUserRepository implements IUserRepository {
  private users: Map<string, User> = new Map();

  async findById(id: string): Promise<User | null> {
    return this.users.get(id) ?? null;
  }

  async findByEmail(email: string): Promise<User | null> {
    for (const u of this.users.values()) {
      if (u.email === email) return u;
    }
    return null;
  }

  async save(user: User): Promise<void> {
    this.users.set(user.id, user);
  }
}

describe('User Domain Entity', () => {
  it('should create a valid user instance', () => {
    const user = new User({
      id: 'usr-1',
      email: 'test@example.com',
      name: 'Jane Doe',
      role: 'user',
      createdAt: new Date(),
    });

    expect(user.id).toBe('usr-1');
    expect(user.email).toBe('test@example.com');
    expect(user.name).toBe('Jane Doe');
    expect(user.role).toBe('user');
  });

  it('should throw error for invalid email format', () => {
    expect(() => {
      new User({
        id: 'usr-2',
        email: 'invalid-email',
        name: 'John Doe',
        role: 'user',
        createdAt: new Date(),
      });
    }).toThrow('Invalid email address format');
  });
});

describe('CreateUserUseCase', () => {
  it('should successfully create and store a new user', async () => {
    const repo = new InMemoryUserRepository();
    const useCase = new CreateUserUseCase(repo);

    const user = await useCase.execute({
      id: 'usr-100',
      email: 'alice@example.com',
      name: 'Alice Cooper',
    });

    expect(user.id).toBe('usr-100');
    const stored = await repo.findById('usr-100');
    expect(stored).not.toBeNull();
    expect(stored?.name).toBe('Alice Cooper');
  });
});
