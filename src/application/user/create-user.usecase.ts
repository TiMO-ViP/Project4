import { User, type IUserRepository } from '../../domain/user/user.ts';

export interface CreateUserDTO {
  id: string;
  email: string;
  name: string;
  role?: 'admin' | 'user' | 'guest';
}

export class CreateUserUseCase {
  private userRepository: IUserRepository;

  constructor(userRepository: IUserRepository) {
    this.userRepository = userRepository;
  }

  async execute(dto: CreateUserDTO): Promise<User> {
    const existing = await this.userRepository.findByEmail(dto.email);
    if (existing) {
      throw new Error(`User with email '${dto.email}' already exists.`);
    }

    const user = new User({
      id: dto.id,
      email: dto.email,
      name: dto.name,
      role: dto.role ?? 'user',
      createdAt: new Date(),
    });

    await this.userRepository.save(user);
    return user;
  }
}
