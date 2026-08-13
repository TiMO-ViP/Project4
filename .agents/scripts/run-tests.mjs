import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { User } from '../../src/domain/user/user.ts';
import { CreateUserUseCase } from '../../src/application/user/create-user.usecase.ts';
import { GetUserProfileUseCase } from '../../src/application/user/get-user-profile.usecase.ts';
import '../../tests/unit/telemetry/tracer.test.mjs';


class InMemoryUserRepository {
  constructor() {
    this.users = new Map();
  }

  async findById(id) {
    return this.users.get(id) ?? null;
  }

  async findByEmail(email) {
    for (const u of this.users.values()) {
      if (u.email === email) return u;
    }
    return null;
  }

  async save(user) {
    this.users.set(user.id, user);
  }
}

describe('User Domain Entity & Use Cases', () => {
  it('should create a valid user instance', () => {
    const user = new User({
      id: 'usr-1',
      email: 'test@example.com',
      name: 'Jane Doe',
      role: 'user',
      createdAt: new Date(),
    });

    assert.equal(user.id, 'usr-1');
    assert.equal(user.email, 'test@example.com');
    assert.equal(user.name, 'Jane Doe');
    assert.equal(user.role, 'user');
  });

  it('should throw error for invalid email format', () => {
    assert.throws(() => {
      new User({
        id: 'usr-2',
        email: 'invalid-email',
        name: 'John Doe',
        role: 'user',
        createdAt: new Date(),
      });
    }, /Invalid email address format/);
  });

  it('should successfully create and store a new user via CreateUserUseCase', async () => {
    const repo = new InMemoryUserRepository();
    const useCase = new CreateUserUseCase(repo);

    const user = await useCase.execute({
      id: 'usr-100',
      email: 'alice@example.com',
      name: 'Alice Cooper',
    });

    assert.equal(user.id, 'usr-100');
    const stored = await repo.findById('usr-100');
    assert.notEqual(stored, null);
    assert.equal(stored.name, 'Alice Cooper');
  });

  it('should successfully retrieve user profile by ID', async () => {
    const repo = new InMemoryUserRepository();
    const createUseCase = new CreateUserUseCase(repo);
    await createUseCase.execute({
      id: 'usr-200',
      email: 'bob@example.com',
      name: 'Bob Smith',
    });

    const getUseCase = new GetUserProfileUseCase(repo);
    const profile = await getUseCase.execute('usr-200');

    assert.equal(profile.id, 'usr-200');
    assert.equal(profile.email, 'bob@example.com');
    assert.equal(profile.name, 'Bob Smith');
  });

  it('should throw error when requesting non-existent user profile', async () => {
    const repo = new InMemoryUserRepository();
    const getUseCase = new GetUserProfileUseCase(repo);

    await assert.rejects(async () => {
      await getUseCase.execute('usr-999');
    }, /User with ID 'usr-999' not found/);
  });
});
