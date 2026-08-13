/**
 * Shared functional utilities across monorepo packages.
 */

/**
 * Asserts at compile time and runtime that an exhaustive check has been completed.
 */
export function assertNever(value: never, message?: string): never {
  throw new Error(
    message ?? `Unexpected unreachable value encountered in assertNever: ${JSON.stringify(value)}`
  );
}

/**
 * Recursively freezes an object and its nested properties.
 */
export function deepFreeze<T extends object>(obj: T): Readonly<T> {
  const propNames = Reflect.ownKeys(obj);

  for (const name of propNames) {
    const value = Reflect.get(obj, name);
    if (value && (typeof value === 'object' || typeof value === 'function')) {
      deepFreeze(value as object);
    }
  }

  return Object.freeze(obj);
}

/**
 * Type guard utility to filter out null and undefined values.
 */
export function isNonNullable<T>(value: T): value is NonNullable<T> {
  return value !== null && value !== undefined;
}
