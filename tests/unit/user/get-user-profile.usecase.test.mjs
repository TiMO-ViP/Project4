import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { User, type IUserRepository } from '../../../src/domain/user/user.ts';
import { CreateUserUseCase } from '../../../src/application/user/create-user.usecase.ts';
import { GetUserProfileUseCase } from '../../../src/application/user/get-user-profile.usecase.ts';

class InMemoryUserRepository implements IUserRepository {
  private users = new Map<string, User>();

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

describe('GetUserProfileUseCase Unit Tests', () => {
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
