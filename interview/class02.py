# 在Python编程中，类方法、静态方法和实例方法是三种不同类型的方法，它们在定义、调用方式以及作用上有所不同。以下是它们的区别和用法：
#
# 1. 实例方法
# ‌定义‌：实例方法是属于类的实例（对象）的方法，它们定义在类中，并且第一个参数通常是self，用于引用实例自身。
#
# ‌用法‌：
#
# 通过实例调用。
# 可以访问和修改实例的属性。
# ‌示例‌：
#
# python
# Copy Code
# class MyClass:
#     def instance_method(self):
#         print("This is an instance method.")
#
# obj = MyClass()
# obj.instance_method()  # 输出: This is an instance method.
# 2. 类方法
# ‌定义‌：类方法是属于类本身的方法，它们用@classmethod装饰器来标识，并且第一个参数是cls，用于引用类本身。
#
# ‌用法‌：
#
# 可以通过类名或实例调用。
# 不能访问实例属性，但可以访问类属性。
# 常用于实现一些涉及类层次操作的功能，如修改类属性。
# ‌示例‌：
#
# python
# Copy Code
# class MyClass:
#     class_attribute = "Class Attribute"
#
#     @classmethod
#     def class_method(cls):
#         print(f"This is a class method. Class attribute: {cls.class_attribute}")
#
# MyClass.class_method()  # 输出: This is a class method. Class attribute: Class Attribute
# obj = MyClass()
# obj.class_method()  # 同样输出: This is a class method. Class attribute: Class Attribute
# 3. 静态方法
# ‌定义‌：静态方法也是属于类本身的方法，但它们用@staticmethod装饰器来标识，不需要特殊的第一个参数（如self或cls）。
#
# ‌用法‌：
#
# 可以通过类名或实例调用。
# 不能访问实例属性和类属性。
# 相当于类命名空间中的一个普通函数，常用于实现一些与类相关但不需要访问类属性或实例属性的功能。
# ‌示例‌：
#
# python
# Copy Code
# class MyClass:
#     @staticmethod
#     def static_method():
#         print("This is a static method.")
#
# MyClass.static_method()  # 输出: This is a static method.
# obj = MyClass()
# obj.static_method()  # 同样输出: This is a static method.
# 总结
# ‌实例方法‌：用self，通过实例调用，可以访问和修改实例属性。
# ‌类方法‌：用@classmethod和cls，通过类或实例调用，可以访问类属性但不能访问实例属性。
# ‌静态方法‌：用@staticmethod，通过类或实例调用，不能访问实例属性和类属性。
# 了解这些方法的区别和用法，有助于在设计类时选择最合适的方法类型，从而实现更清晰、更合理的类结构。