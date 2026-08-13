import type { User, IUserRepository } from '../../domain/user/user.ts';

export class GetUserProfileUseCase {
  private userRepository: IUserRepository;

  constructor(userRepository: IUserRepository) {
    this.userRepository = userRepository;
  }

  async execute(userId: string): Promise<User> {
    const user = await this.userRepository.findById(userId);
    if (!user) {
      throw new Error(`User with ID '${userId}' not found.`);
    }
    return user;
  }
}
