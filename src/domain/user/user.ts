export interface UserProps {
  id: string;
  email: string;
  name: string;
  role: 'admin' | 'user' | 'guest';
  createdAt: Date;
}

export class User {
  private props: UserProps;

  constructor(props: UserProps) {
    if (!props.email.includes('@')) {
      throw new Error('Invalid email address format');
    }
    if (props.name.trim().length === 0) {
      throw new Error('User name cannot be empty');
    }
    this.props = props;
  }

  get id(): string {
    return this.props.id;
  }

  get email(): string {
    return this.props.email;
  }

  get name(): string {
    return this.props.name;
  }

  get role(): string {
    return this.props.role;
  }

  get createdAt(): Date {
    return this.props.createdAt;
  }

  public toJSON(): UserProps {
    return { ...this.props };
  }
}

export interface IUserRepository {
  findById(id: string): Promise<User | null>;
  findByEmail(email: string): Promise<User | null>;
  save(user: User): Promise<void>;
}
