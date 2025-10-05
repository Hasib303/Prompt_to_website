import config
import torch
from ctransformers import LLM


def load_llm_model():
    """Load the LLM model for code generation"""
    try:
        print("Loading LLM model...")
        print(f"Model: {config.LLM_MODEL}")
        
        if config.LLM_MODEL.startswith('Qwen/'):
            print("Using Qwen model via transformers...")
            from transformers import AutoTokenizer, AutoModelForCausalLM
            tokenizer = AutoTokenizer.from_pretrained(
                config.LLM_MODEL,
                trust_remote_code=True
            )
            dtype = torch.float16 if (hasattr(torch, 'cuda') and torch.cuda.is_available()) else torch.float32
            model = AutoModelForCausalLM.from_pretrained(
                config.LLM_MODEL,
                trust_remote_code=True,
                torch_dtype=dtype,
                device_map='auto',
                low_cpu_mem_usage=True
            )
            return {'tokenizer': tokenizer, 'model': model, 'type': 'qwen'}
        else:
            from transformers import AutoTokenizer, AutoModelForCausalLM
            tokenizer = AutoTokenizer.from_pretrained(config.LLM_MODEL)
            model = AutoModelForCausalLM.from_pretrained(config.LLM_MODEL)
            return {'tokenizer': tokenizer, 'model': model, 'type': 'transformers'}
            
    except Exception as e:
        print(f"⚠️ Failed to load LLM model: {e}")
        return None


def create_structured_website(user_query, retrieved_components):
    """Create a complete, structured website using template + components"""
    
    query_lower = user_query.lower()
    
    if any(word in query_lower for word in ['portfolio', 'resume', 'cv']):
        website_type = 'portfolio'
    elif any(word in query_lower for word in ['blog', 'article', 'news']):
        website_type = 'blog'
    elif any(word in query_lower for word in ['shop', 'store', 'ecommerce', 'product']):
        website_type = 'ecommerce'
    elif any(word in query_lower for word in ['landing', 'marketing', 'startup']):
        website_type = 'landing'
    else:
        website_type = 'general'
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{user_query}</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50">
'''
    
    html += create_header(website_type, retrieved_components)
    
    html += create_hero(website_type, user_query, retrieved_components)
    
    html += create_main_content(website_type, retrieved_components)
    
    html += create_footer(website_type, retrieved_components)
    
    html += '''
</body>
</html>'''
    
    return html


def create_header(website_type, components):
    """Create a proper header with navigation"""
    nav_items = ['Home', 'About', 'Services', 'Contact']
    if website_type == 'portfolio':
        nav_items = ['Home', 'About', 'Projects', 'Contact']
    elif website_type == 'blog':
        nav_items = ['Home', 'Articles', 'Categories', 'About']
    elif website_type == 'ecommerce':
        nav_items = ['Home', 'Products', 'Cart', 'Account']
    
    header = f'''
    <!-- Header -->
    <header class="bg-white shadow-sm sticky top-0 z-50">
        <nav class="container mx-auto px-6 py-4">
            <div class="flex items-center justify-between">
                <div class="text-2xl font-bold text-blue-600">Brand</div>
                <div class="hidden md:flex space-x-8">
'''
    
    for item in nav_items:
        header += f'                    <a href="#{item.lower()}" class="text-gray-700 hover:text-blue-600 transition">{item}</a>\n'
    
    header += '''                </div>
                <button class="md:hidden text-gray-700">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
                    </svg>
                </button>
            </div>
        </nav>
    </header>
'''
    return header


def create_hero(website_type, query, components):
    """Create hero section based on website type"""
    if website_type == 'portfolio':
        hero = '''
    <!-- Hero Section -->
    <section class="bg-gradient-to-r from-blue-600 to-purple-600 text-white py-20">
        <div class="container mx-auto px-6">
            <div class="max-w-3xl">
                <h1 class="text-5xl font-bold mb-4">Hi, I'm John Doe</h1>
                <p class="text-xl mb-8">Full Stack Developer & UI/UX Designer</p>
                <p class="text-lg mb-8 opacity-90">I create beautiful, functional websites and applications that solve real problems.</p>
                <div class="flex space-x-4">
                    <button class="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100 transition">View Projects</button>
                    <button class="border-2 border-white text-white px-8 py-3 rounded-lg font-semibold hover:bg-white hover:text-blue-600 transition">Contact Me</button>
                </div>
            </div>
        </div>
    </section>
'''
    elif website_type == 'blog':
        hero = '''
    <!-- Hero Section -->
    <section class="bg-gradient-to-r from-green-600 to-teal-600 text-white py-20">
        <div class="container mx-auto px-6 text-center">
            <h1 class="text-5xl font-bold mb-4">Tech Blog</h1>
            <p class="text-xl mb-8">Insights, tutorials, and stories about web development</p>
            <div class="max-w-xl mx-auto">
                <div class="relative">
                    <input type="text" placeholder="Search articles..." class="w-full px-6 py-4 rounded-lg text-gray-800 focus:outline-none focus:ring-2 focus:ring-white"/>
                    <button class="absolute right-2 top-2 bg-green-600 text-white px-6 py-2 rounded-lg">Search</button>
                </div>
            </div>
        </div>
    </section>
'''
    else:
        hero = f'''
    <!-- Hero Section -->
    <section class="bg-gradient-to-r from-blue-600 to-indigo-600 text-white py-20">
        <div class="container mx-auto px-6 text-center">
            <h1 class="text-5xl font-bold mb-4">{query}</h1>
            <p class="text-xl mb-8">Professional, modern, and responsive solution</p>
            <button class="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100 transition">Get Started</button>
        </div>
    </section>
'''
    return hero


def create_main_content(website_type, components):
    """Create main content sections with retrieved components"""
    content = '<main class="container mx-auto px-6 py-12">\n'
    
    if website_type == 'portfolio':
        content += create_portfolio_sections(components)
    elif website_type == 'blog':
        content += create_blog_sections(components)
    elif website_type == 'ecommerce':
        content += create_ecommerce_sections(components)
    else:
        content += create_general_sections(components)
    
    content += '</main>\n'
    return content


def create_portfolio_sections(components):
    """Create portfolio-specific sections"""
    sections = '''
    <!-- About Section -->
    <section id="about" class="mb-16">
        <h2 class="text-3xl font-bold text-gray-800 mb-6">About Me</h2>
        <div class="bg-white rounded-lg shadow-md p-8">
            <p class="text-gray-600 mb-4">I'm a passionate developer with 5+ years of experience building web applications. I specialize in React, Node.js, and modern web technologies.</p>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-8">
                <div class="text-center">
                    <div class="text-4xl font-bold text-blue-600 mb-2">50+</div>
                    <div class="text-gray-600">Projects Completed</div>
                </div>
                <div class="text-center">
                    <div class="text-4xl font-bold text-blue-600 mb-2">30+</div>
                    <div class="text-gray-600">Happy Clients</div>
                </div>
                <div class="text-center">
                    <div class="text-4xl font-bold text-blue-600 mb-2">5+</div>
                    <div class="text-gray-600">Years Experience</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="mb-16">
        <h2 class="text-3xl font-bold text-gray-800 mb-6">Featured Projects</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition">
                <div class="h-48 bg-gradient-to-r from-blue-500 to-purple-500"></div>
                <div class="p-6">
                    <h3 class="text-xl font-bold text-gray-800 mb-2">E-commerce Platform</h3>
                    <p class="text-gray-600 mb-4">Full-stack e-commerce solution with React and Node.js</p>
                    <div class="flex flex-wrap gap-2">
                        <span class="bg-blue-100 text-blue-800 text-xs px-3 py-1 rounded-full">React</span>
                        <span class="bg-green-100 text-green-800 text-xs px-3 py-1 rounded-full">Node.js</span>
                    </div>
                </div>
            </div>
            <div class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition">
                <div class="h-48 bg-gradient-to-r from-green-500 to-teal-500"></div>
                <div class="p-6">
                    <h3 class="text-xl font-bold text-gray-800 mb-2">Analytics Dashboard</h3>
                    <p class="text-gray-600 mb-4">Real-time data visualization dashboard</p>
                    <div class="flex flex-wrap gap-2">
                        <span class="bg-blue-100 text-blue-800 text-xs px-3 py-1 rounded-full">Vue.js</span>
                        <span class="bg-yellow-100 text-yellow-800 text-xs px-3 py-1 rounded-full">D3.js</span>
                    </div>
                </div>
            </div>
            <div class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition">
                <div class="h-48 bg-gradient-to-r from-pink-500 to-red-500"></div>
                <div class="p-6">
                    <h3 class="text-xl font-bold text-gray-800 mb-2">Mobile App</h3>
                    <p class="text-gray-600 mb-4">Cross-platform mobile application</p>
                    <div class="flex flex-wrap gap-2">
                        <span class="bg-blue-100 text-blue-800 text-xs px-3 py-1 rounded-full">React Native</span>
                        <span class="bg-purple-100 text-purple-800 text-xs px-3 py-1 rounded-full">Firebase</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="mb-16">
        <h2 class="text-3xl font-bold text-gray-800 mb-6">Skills & Technologies</h2>
        <div class="bg-white rounded-lg shadow-md p-8">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                <div class="text-center">
                    <div class="text-4xl mb-2">⚛️</div>
                    <div class="font-semibold">React</div>
                </div>
                <div class="text-center">
                    <div class="text-4xl mb-2">📗</div>
                    <div class="font-semibold">Node.js</div>
                </div>
                <div class="text-center">
                    <div class="text-4xl mb-2">🎨</div>
                    <div class="font-semibold">Tailwind CSS</div>
                </div>
                <div class="text-center">
                    <div class="text-4xl mb-2">🗄️</div>
                    <div class="font-semibold">MongoDB</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="mb-16">
        <h2 class="text-3xl font-bold text-gray-800 mb-6">Get In Touch</h2>
        <div class="bg-white rounded-lg shadow-md p-8">
            <form class="space-y-6">
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Name</label>
                    <input type="text" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent" placeholder="Your name"/>
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Email</label>
                    <input type="email" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent" placeholder="your@email.com"/>
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Message</label>
                    <textarea rows="4" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent" placeholder="Your message"></textarea>
                </div>
                <button type="submit" class="bg-blue-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-blue-700 transition">Send Message</button>
            </form>
        </div>
    </section>
'''
    return sections


def create_blog_sections(components):
    """Create blog-specific sections"""
    return '''
    <!-- Featured Posts -->
    <section class="mb-16">
        <h2 class="text-3xl font-bold text-gray-800 mb-6">Latest Articles</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <article class="bg-white rounded-lg shadow-md overflow-hidden">
                <div class="h-48 bg-gradient-to-r from-blue-500 to-purple-500"></div>
                <div class="p-6">
                    <div class="flex items-center space-x-2 text-sm text-gray-500 mb-2">
                        <span>May 15, 2024</span>
                        <span>•</span>
                        <span>5 min read</span>
                    </div>
                    <h3 class="text-2xl font-bold text-gray-800 mb-3">Getting Started with React Hooks</h3>
                    <p class="text-gray-600 mb-4">Learn how to use React Hooks to manage state and side effects in your functional components.</p>
                    <a href="#" class="text-blue-600 font-semibold hover:text-blue-700">Read More →</a>
                </div>
            </article>
            <article class="bg-white rounded-lg shadow-md overflow-hidden">
                <div class="h-48 bg-gradient-to-r from-green-500 to-teal-500"></div>
                <div class="p-6">
                    <div class="flex items-center space-x-2 text-sm text-gray-500 mb-2">
                        <span>May 10, 2024</span>
                        <span>•</span>
                        <span>8 min read</span>
                    </div>
                    <h3 class="text-2xl font-bold text-gray-800 mb-3">Building RESTful APIs with Node.js</h3>
                    <p class="text-gray-600 mb-4">A comprehensive guide to creating scalable REST APIs using Express and Node.js.</p>
                    <a href="#" class="text-blue-600 font-semibold hover:text-blue-700">Read More →</a>
                </div>
            </article>
        </div>
    </section>

    <!-- Categories -->
    <section class="mb-16">
        <h2 class="text-3xl font-bold text-gray-800 mb-6">Browse by Category</h2>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
            <a href="#" class="bg-white p-6 rounded-lg shadow-md text-center hover:shadow-xl transition">
                <div class="text-3xl mb-2">⚛️</div>
                <div class="font-semibold text-gray-800">React</div>
                <div class="text-sm text-gray-500">24 posts</div>
            </a>
            <a href="#" class="bg-white p-6 rounded-lg shadow-md text-center hover:shadow-xl transition">
                <div class="text-3xl mb-2">📗</div>
                <div class="font-semibold text-gray-800">Node.js</div>
                <div class="text-sm text-gray-500">18 posts</div>
            </a>
            <a href="#" class="bg-white p-6 rounded-lg shadow-md text-center hover:shadow-xl transition">
                <div class="text-3xl mb-2">🎨</div>
                <div class="font-semibold text-gray-800">CSS</div>
                <div class="text-sm text-gray-500">15 posts</div>
            </a>
            <a href="#" class="bg-white p-6 rounded-lg shadow-md text-center hover:shadow-xl transition">
                <div class="text-3xl mb-2">🗄️</div>
                <div class="font-semibold text-gray-800">Database</div>
                <div class="text-sm text-gray-500">12 posts</div>
            </a>
        </div>
    </section>
'''


def create_ecommerce_sections(components):
    """Create e-commerce sections"""
    return '''
    <!-- Products Grid -->
    <section class="mb-16">
        <h2 class="text-3xl font-bold text-gray-800 mb-6">Featured Products</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6">
            <div class="bg-white rounded-lg shadow-md overflow-hidden group">
                <div class="h-64 bg-gray-200 relative overflow-hidden">
                    <div class="absolute inset-0 bg-gradient-to-br from-blue-400 to-purple-500"></div>
                </div>
                <div class="p-4">
                    <h3 class="font-semibold text-gray-800 mb-1">Product Name</h3>
                    <p class="text-sm text-gray-500 mb-2">Category</p>
                    <div class="flex items-center justify-between">
                        <span class="text-xl font-bold text-blue-600">$99.99</span>
                        <button class="bg-blue-600 text-white px-4 py-2 rounded-lg text-sm hover:bg-blue-700">Add to Cart</button>
                    </div>
                </div>
            </div>
            <div class="bg-white rounded-lg shadow-md overflow-hidden group">
                <div class="h-64 bg-gray-200 relative overflow-hidden">
                    <div class="absolute inset-0 bg-gradient-to-br from-green-400 to-teal-500"></div>
                </div>
                <div class="p-4">
                    <h3 class="font-semibold text-gray-800 mb-1">Product Name</h3>
                    <p class="text-sm text-gray-500 mb-2">Category</p>
                    <div class="flex items-center justify-between">
                        <span class="text-xl font-bold text-blue-600">$79.99</span>
                        <button class="bg-blue-600 text-white px-4 py-2 rounded-lg text-sm hover:bg-blue-700">Add to Cart</button>
                    </div>
                </div>
            </div>
            <div class="bg-white rounded-lg shadow-md overflow-hidden group">
                <div class="h-64 bg-gray-200 relative overflow-hidden">
                    <div class="absolute inset-0 bg-gradient-to-br from-pink-400 to-red-500"></div>
                </div>
                <div class="p-4">
                    <h3 class="font-semibold text-gray-800 mb-1">Product Name</h3>
                    <p class="text-sm text-gray-500 mb-2">Category</p>
                    <div class="flex items-center justify-between">
                        <span class="text-xl font-bold text-blue-600">$129.99</span>
                        <button class="bg-blue-600 text-white px-4 py-2 rounded-lg text-sm hover:bg-blue-700">Add to Cart</button>
                    </div>
                </div>
            </div>
            <div class="bg-white rounded-lg shadow-md overflow-hidden group">
                <div class="h-64 bg-gray-200 relative overflow-hidden">
                    <div class="absolute inset-0 bg-gradient-to-br from-yellow-400 to-orange-500"></div>
                </div>
                <div class="p-4">
                    <h3 class="font-semibold text-gray-800 mb-1">Product Name</h3>
                    <p class="text-sm text-gray-500 mb-2">Category</p>
                    <div class="flex items-center justify-between">
                        <span class="text-xl font-bold text-blue-600">$89.99</span>
                        <button class="bg-blue-600 text-white px-4 py-2 rounded-lg text-sm hover:bg-blue-700">Add to Cart</button>
                    </div>
                </div>
            </div>
        </div>
    </section>
'''


def create_general_sections(components):
    """Create general website sections"""
    return '''
    <!-- Features Section -->
    <section class="mb-16">
        <h2 class="text-3xl font-bold text-gray-800 mb-6 text-center">Our Features</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="bg-white p-8 rounded-lg shadow-md text-center">
                <div class="text-5xl mb-4">🚀</div>
                <h3 class="text-xl font-bold text-gray-800 mb-3">Fast Performance</h3>
                <p class="text-gray-600">Lightning-fast loading times and optimized performance.</p>
            </div>
            <div class="bg-white p-8 rounded-lg shadow-md text-center">
                <div class="text-5xl mb-4">🎨</div>
                <h3 class="text-xl font-bold text-gray-800 mb-3">Beautiful Design</h3>
                <p class="text-gray-600">Modern, clean, and responsive user interface.</p>
            </div>
            <div class="bg-white p-8 rounded-lg shadow-md text-center">
                <div class="text-5xl mb-4">🔒</div>
                <h3 class="text-xl font-bold text-gray-800 mb-3">Secure</h3>
                <p class="text-gray-600">Enterprise-level security and data protection.</p>
            </div>
        </div>
    </section>

    <!-- Content Section -->
    <section class="mb-16">
        <div class="bg-white rounded-lg shadow-md p-8">
            <h2 class="text-2xl font-bold text-gray-800 mb-4">About Our Service</h2>
            <p class="text-gray-600 mb-4">We provide professional, reliable, and innovative solutions to help your business grow. Our team is dedicated to delivering the highest quality results.</p>
            <p class="text-gray-600 mb-6">With years of experience and a proven track record, we're the partner you can trust for all your needs.</p>
            <button class="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition">Learn More</button>
        </div>
    </section>
'''


def create_footer(website_type, components):
    """Create footer section"""
    return '''
    <!-- Footer -->
    <footer class="bg-gray-800 text-white py-12">
        <div class="container mx-auto px-6">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
                <div>
                    <h3 class="text-xl font-bold mb-4">Brand</h3>
                    <p class="text-gray-400">Building amazing web experiences.</p>
                </div>
                <div>
                    <h4 class="font-semibold mb-4">Quick Links</h4>
                    <ul class="space-y-2">
                        <li><a href="#" class="text-gray-400 hover:text-white">Home</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">About</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">Services</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">Contact</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="font-semibold mb-4">Resources</h4>
                    <ul class="space-y-2">
                        <li><a href="#" class="text-gray-400 hover:text-white">Blog</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">Documentation</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">Support</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">FAQ</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="font-semibold mb-4">Follow Us</h4>
                    <div class="flex space-x-4">
                        <a href="#" class="text-gray-400 hover:text-white">Twitter</a>
                        <a href="#" class="text-gray-400 hover:text-white">GitHub</a>
                        <a href="#" class="text-gray-400 hover:text-white">LinkedIn</a>
                    </div>
                </div>
            </div>
            <div class="border-t border-gray-700 mt-8 pt-8 text-center text-gray-400">
                <p>&copy; 2024 Brand. All rights reserved.</p>
            </div>
        </div>
    </footer>
'''


def generate_website_code(user_query, retrieved_components):
    """Main function to generate complete website code"""
    print(f"\nGenerating website for: {user_query}")
    print(f"Using {len(retrieved_components)} relevant components\n")
    
    # Always use structured generation for complete output
    print("✅ Using structured template generation for complete HTML")
    html_code = create_structured_website(user_query, retrieved_components)
    
    return html_code