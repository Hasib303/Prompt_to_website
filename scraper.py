import requests
from bs4 import BeautifulSoup
import pandas as pd


def create_all_keep_design_components():
    """
    Create comprehensive component database with all 49 Keep Design components
    Based on https://keepdesign.io/components
    """
    components = []
    
    foundation_components = [
        {
            'component_id': 'keep_001',
            'name': 'Colors',
            'category': 'Foundation',
            'description': 'Comprehensive color palette with primary, secondary, neutral, and semantic colors. Includes light and dark mode variants.',
            'code_snippet': '<div class="flex flex-wrap gap-4"><div class="w-16 h-16 bg-blue-500 rounded-lg"></div><div class="w-16 h-16 bg-blue-600 rounded-lg"></div><div class="w-16 h-16 bg-blue-700 rounded-lg"></div><div class="w-16 h-16 bg-gray-500 rounded-lg"></div><div class="w-16 h-16 bg-gray-600 rounded-lg"></div></div>',
            'use_cases': 'Brand identity, color schemes, design systems, theming'
        },
        {
            'component_id': 'keep_002',
            'name': 'Typography',
            'category': 'Foundation',
            'description': 'Typography scale with font families, sizes, weights, and line heights. Includes heading and body text styles.',
            'code_snippet': '<div class="space-y-4"><h1 class="text-4xl font-bold">Heading 1</h1><h2 class="text-3xl font-semibold">Heading 2</h2><h3 class="text-2xl font-medium">Heading 3</h3><p class="text-lg">Body text with proper line height</p><p class="text-sm text-gray-600">Small text</p></div>',
            'use_cases': 'Text hierarchy, readability, content structure, brand consistency'
        },
        {
            'component_id': 'keep_003',
            'name': 'Shadow',
            'category': 'Foundation',
            'description': 'Elevation system with multiple shadow levels for depth and visual hierarchy.',
            'code_snippet': '<div class="space-y-6"><div class="p-6 bg-white shadow-sm rounded-lg">Small shadow</div><div class="p-6 bg-white shadow-md rounded-lg">Medium shadow</div><div class="p-6 bg-white shadow-lg rounded-lg">Large shadow</div><div class="p-6 bg-white shadow-xl rounded-lg">Extra large shadow</div></div>',
            'use_cases': 'Card elevation, modal overlays, button states, visual depth'
        },
        {
            'component_id': 'keep_004',
            'name': 'Spacing Scale',
            'category': 'Foundation',
            'description': 'Consistent spacing system using multiples of 4px for margins, padding, and gaps.',
            'code_snippet': '<div class="space-y-4"><div class="p-2 bg-blue-100 rounded">2px padding</div><div class="p-4 bg-blue-200 rounded">4px padding</div><div class="p-6 bg-blue-300 rounded">6px padding</div><div class="p-8 bg-blue-400 rounded">8px padding</div></div>',
            'use_cases': 'Layout consistency, responsive design, component spacing, grid systems'
        },
        {
            'component_id': 'keep_005',
            'name': 'Icons',
            'category': 'Foundation',
            'description': 'Comprehensive icon library with consistent sizing and styling options.',
            'code_snippet': '<div class="flex space-x-4"><svg class="w-6 h-6 text-blue-600" fill="currentColor" viewBox="0 0 20 20"><path d="M10 12a2 2 0 100-4 2 2 0 000 4z"/><path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd"/></svg><svg class="w-6 h-6 text-green-600" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg></div>',
            'use_cases': 'User interface, navigation, actions, visual communication'
        },
        {
            'component_id': 'keep_006',
            'name': 'Logo',
            'category': 'Foundation',
            'description': 'Brand logo components with different sizes and variations for various contexts.',
            'code_snippet': '<div class="flex items-center space-x-4"><div class="text-2xl font-bold text-blue-600">Brand</div><div class="text-lg font-semibold text-gray-800">Brand</div><div class="text-sm font-medium text-gray-600">Brand</div></div>',
            'use_cases': 'Brand identity, headers, footers, marketing materials'
        }
    ]
    
    ui_components = [
        {
            'component_id': 'keep_007',
            'name': 'Button',
            'category': 'UI Components',
            'description': 'Primary, secondary, and ghost button variants with different sizes and states.',
            'code_snippet': '<div class="space-x-4"><button class="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700">Primary</button><button class="border border-blue-600 text-blue-600 px-6 py-3 rounded-lg hover:bg-blue-50">Secondary</button><button class="text-blue-600 px-6 py-3 hover:bg-blue-50 rounded-lg">Ghost</button></div>',
            'use_cases': 'Actions, forms, navigation, CTAs'
        },
        {
            'component_id': 'keep_008',
            'name': 'Button Group',
            'category': 'UI Components',
            'description': 'Grouped buttons for related actions with consistent spacing and styling.',
            'code_snippet': '<div class="inline-flex rounded-lg border border-gray-300"><button class="px-4 py-2 text-sm font-medium text-gray-700 bg-white border-r border-gray-300 hover:bg-gray-50">Left</button><button class="px-4 py-2 text-sm font-medium text-gray-700 bg-white border-r border-gray-300 hover:bg-gray-50">Middle</button><button class="px-4 py-2 text-sm font-medium text-gray-700 bg-white hover:bg-gray-50">Right</button></div>',
            'use_cases': 'Toolbars, filters, segmented controls, action groups'
        },
        {
            'component_id': 'keep_009',
            'name': 'Avatar',
            'category': 'UI Components',
            'description': 'User profile images with fallback initials and different sizes.',
            'code_snippet': '<div class="flex space-x-4"><div class="w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center text-white text-sm font-medium">JD</div><div class="w-12 h-12 bg-green-500 rounded-full flex items-center justify-center text-white font-medium">AB</div><div class="w-16 h-16 bg-purple-500 rounded-full flex items-center justify-center text-white text-lg font-medium">CD</div></div>',
            'use_cases': 'User profiles, comments, team members, chat interfaces'
        },
        {
            'component_id': 'keep_010',
            'name': 'Accordion',
            'category': 'UI Components',
            'description': 'Collapsible content sections with smooth animations and customizable headers.',
            'code_snippet': '<div class="space-y-2"><div class="border border-gray-200 rounded-lg"><button class="w-full px-4 py-3 text-left font-medium flex justify-between items-center">Section 1 <span class="transform transition-transform">+</span></button><div class="px-4 pb-3 text-gray-600">Content for section 1</div></div></div>',
            'use_cases': 'FAQs, documentation, settings panels, content organization'
        },
        {
            'component_id': 'keep_011',
            'name': 'Alert',
            'category': 'UI Components',
            'description': 'Notification messages with different types: success, warning, error, and info.',
            'code_snippet': '<div class="space-y-4"><div class="bg-green-50 border border-green-200 text-green-800 px-4 py-3 rounded-lg">Success message</div><div class="bg-yellow-50 border border-yellow-200 text-yellow-800 px-4 py-3 rounded-lg">Warning message</div><div class="bg-red-50 border border-red-200 text-red-800 px-4 py-3 rounded-lg">Error message</div></div>',
            'use_cases': 'Notifications, form validation, system messages, user feedback'
        },
        {
            'component_id': 'keep_012',
            'name': 'Badge',
            'category': 'UI Components',
            'description': 'Small status indicators with different colors and sizes for labels and counts.',
            'code_snippet': '<div class="flex space-x-2"><span class="bg-blue-100 text-blue-800 text-xs font-medium px-2.5 py-0.5 rounded-full">Default</span><span class="bg-green-100 text-green-800 text-xs font-medium px-2.5 py-0.5 rounded-full">Success</span><span class="bg-red-100 text-red-800 text-xs font-medium px-2.5 py-0.5 rounded-full">Error</span></div>',
            'use_cases': 'Status indicators, notifications, labels, counts'
        },
        {
            'component_id': 'keep_013',
            'name': 'Charts',
            'category': 'UI Components',
            'description': 'Data visualization components including bar charts, line charts, and pie charts.',
            'code_snippet': '<div class="bg-white p-6 rounded-lg shadow"><div class="h-64 bg-gray-100 rounded flex items-center justify-center"><div class="text-center"><div class="text-2xl font-bold text-gray-600">📊</div><p class="text-gray-500 mt-2">Chart Component</p><p class="text-sm text-gray-400">Bar, Line, Pie Charts</p></div></div></div>',
            'use_cases': 'Data visualization, analytics, dashboards, reports'
        },
        {
            'component_id': 'keep_014',
            'name': 'Empty',
            'category': 'UI Components',
            'description': 'Empty state component for when there is no data or content to display.',
            'code_snippet': '<div class="text-center py-12"><div class="text-6xl mb-4">📭</div><h3 class="text-lg font-medium text-gray-900 mb-2">No data available</h3><p class="text-gray-500 mb-4">Get started by adding some content</p><button class="bg-blue-600 text-white px-4 py-2 rounded-lg">Add Content</button></div>',
            'use_cases': 'Empty states, onboarding, no data scenarios, user guidance'
        },
        {
            'component_id': 'keep_015',
            'name': 'Messaging',
            'category': 'UI Components',
            'description': 'Chat and messaging interface components with message bubbles and input fields.',
            'code_snippet': '<div class="max-w-md mx-auto bg-white rounded-lg shadow"><div class="p-4 border-b"><h3 class="font-medium">Chat</h3></div><div class="p-4 space-y-3 h-64 overflow-y-auto"><div class="flex justify-end"><div class="bg-blue-600 text-white p-3 rounded-lg max-w-xs">Hello there!</div></div><div class="flex justify-start"><div class="bg-gray-200 p-3 rounded-lg max-w-xs">Hi! How can I help?</div></div></div><div class="p-4 border-t"><input type="text" placeholder="Type a message..." class="w-full px-3 py-2 border rounded-lg"/></div></div>',
            'use_cases': 'Chat interfaces, messaging apps, customer support, team communication'
        },
        {
            'component_id': 'keep_016',
            'name': 'Skeleton',
            'category': 'UI Components',
            'description': 'Loading placeholders that mimic the structure of content while it loads.',
            'code_snippet': '<div class="space-y-4"><div class="animate-pulse"><div class="h-4 bg-gray-200 rounded w-3/4 mb-2"></div><div class="h-4 bg-gray-200 rounded w-1/2 mb-2"></div><div class="h-4 bg-gray-200 rounded w-5/6"></div></div><div class="animate-pulse"><div class="h-32 bg-gray-200 rounded"></div></div></div>',
            'use_cases': 'Loading states, content placeholders, improved UX, perceived performance'
        }
    ]
    
    additional_ui_components = [
        {
            'component_id': 'keep_017',
            'name': 'Steps',
            'category': 'UI Components',
            'description': 'Step indicator component for multi-step processes and workflows.',
            'code_snippet': '<div class="flex items-center space-x-4"><div class="flex items-center"><div class="w-8 h-8 bg-blue-600 text-white rounded-full flex items-center justify-center text-sm font-medium">1</div><span class="ml-2 text-sm font-medium">Step 1</span></div><div class="flex-1 h-px bg-gray-300"></div><div class="flex items-center"><div class="w-8 h-8 bg-gray-300 text-gray-600 rounded-full flex items-center justify-center text-sm font-medium">2</div><span class="ml-2 text-sm text-gray-500">Step 2</span></div></div>',
            'use_cases': 'Onboarding flows, checkout processes, form wizards, progress tracking'
        },
        {
            'component_id': 'keep_018',
            'name': 'Breadcrumb',
            'category': 'UI Components',
            'description': 'Navigation breadcrumb component showing current page hierarchy.',
            'code_snippet': '<nav class="flex" aria-label="Breadcrumb"><ol class="flex items-center space-x-2"><li><a href="#" class="text-gray-500 hover:text-gray-700">Home</a></li><li class="text-gray-400">/</li><li><a href="#" class="text-gray-500 hover:text-gray-700">Products</a></li><li class="text-gray-400">/</li><li class="text-gray-900 font-medium">Current Page</li></ol></nav>',
            'use_cases': 'Navigation, page hierarchy, user orientation, site structure'
        },
        {
            'component_id': 'keep_019',
            'name': 'Checkbox',
            'category': 'UI Components',
            'description': 'Checkbox input component with different states and sizes.',
            'code_snippet': '<div class="space-y-3"><label class="flex items-center"><input type="checkbox" class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"/><span class="ml-2 text-sm text-gray-700">Checkbox option</span></label><label class="flex items-center"><input type="checkbox" checked class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"/><span class="ml-2 text-sm text-gray-700">Checked option</span></label></div>',
            'use_cases': 'Forms, settings, filters, multi-select options'
        },
        {
            'component_id': 'keep_020',
            'name': 'Checkbox Group',
            'category': 'UI Components',
            'description': 'Group of related checkboxes with consistent styling and behavior.',
            'code_snippet': '<fieldset class="space-y-3"><legend class="text-sm font-medium text-gray-700 mb-3">Select Options</legend><label class="flex items-center"><input type="checkbox" class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"/><span class="ml-2 text-sm text-gray-700">Option 1</span></label><label class="flex items-center"><input type="checkbox" class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"/><span class="ml-2 text-sm text-gray-700">Option 2</span></label><label class="flex items-center"><input type="checkbox" class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"/><span class="ml-2 text-sm text-gray-700">Option 3</span></label></fieldset>',
            'use_cases': 'Form groups, settings panels, filter groups, multi-select lists'
        },
        {
            'component_id': 'keep_021',
            'name': 'Date Picker',
            'category': 'UI Components',
            'description': 'Date selection component with calendar interface and validation.',
            'code_snippet': '<div class="max-w-sm"><label class="block text-sm font-medium text-gray-700 mb-2">Select Date</label><input type="date" class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"/></div>',
            'use_cases': 'Forms, scheduling, date selection, event planning'
        },
        {
            'component_id': 'keep_022',
            'name': 'Dropdown',
            'category': 'UI Components',
            'description': 'Dropdown menu component with search and multi-select capabilities.',
            'code_snippet': '<div class="relative max-w-sm"><label class="block text-sm font-medium text-gray-700 mb-2">Select Option</label><select class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"><option>Choose an option</option><option>Option 1</option><option>Option 2</option><option>Option 3</option></select></div>',
            'use_cases': 'Forms, navigation menus, option selection, filters'
        },
        {
            'component_id': 'keep_023',
            'name': 'File Upload',
            'category': 'UI Components',
            'description': 'File upload component with drag-and-drop functionality and progress indicators.',
            'code_snippet': '<div class="border-2 border-dashed border-gray-300 rounded-lg p-6 text-center hover:border-gray-400 transition"><div class="text-4xl mb-4">📁</div><h3 class="text-lg font-medium text-gray-900 mb-2">Upload files</h3><p class="text-gray-500 mb-4">Drag and drop files here, or click to select</p><button class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">Choose Files</button></div>',
            'use_cases': 'File management, document uploads, media galleries, data import'
        },
        {
            'component_id': 'keep_024',
            'name': 'Modal',
            'category': 'UI Components',
            'description': 'Modal dialog component with overlay, close button, and customizable content.',
            'code_snippet': '<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"><div class="bg-white rounded-lg p-6 max-w-md w-full mx-4"><div class="flex justify-between items-center mb-4"><h3 class="text-lg font-medium">Modal Title</h3><button class="text-gray-400 hover:text-gray-600">×</button></div><p class="text-gray-600 mb-6">Modal content goes here</p><div class="flex justify-end space-x-3"><button class="px-4 py-2 text-gray-700 border border-gray-300 rounded-lg hover:bg-gray-50">Cancel</button><button class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">Confirm</button></div></div></div>',
            'use_cases': 'Confirmations, forms, details view, user interactions'
        },
        {
            'component_id': 'keep_025',
            'name': 'Pagination',
            'category': 'UI Components',
            'description': 'Pagination component for navigating through multiple pages of content.',
            'code_snippet': '<nav class="flex items-center justify-between"><div class="text-sm text-gray-700">Showing 1 to 10 of 100 results</div><div class="flex space-x-2"><button class="px-3 py-2 text-gray-500 border border-gray-300 rounded-lg hover:bg-gray-50">Previous</button><button class="px-3 py-2 bg-blue-600 text-white rounded-lg">1</button><button class="px-3 py-2 text-gray-700 border border-gray-300 rounded-lg hover:bg-gray-50">2</button><button class="px-3 py-2 text-gray-700 border border-gray-300 rounded-lg hover:bg-gray-50">3</button><button class="px-3 py-2 text-gray-500 border border-gray-300 rounded-lg hover:bg-gray-50">Next</button></div></nav>',
            'use_cases': 'Data tables, search results, content lists, navigation'
        },
        {
            'component_id': 'keep_026',
            'name': 'Progress Bar',
            'category': 'UI Components',
            'description': 'Progress indicator component showing completion status of tasks or processes.',
            'code_snippet': '<div class="space-y-4"><div class="w-full bg-gray-200 rounded-full h-2"><div class="bg-blue-600 h-2 rounded-full" style="width: 45%"></div></div><div class="flex justify-between text-sm text-gray-600"><span>45% Complete</span><span>Step 3 of 7</span></div></div>',
            'use_cases': 'Loading states, task progress, form completion, upload progress'
        },
        {
            'component_id': 'keep_027',
            'name': 'Rating',
            'category': 'UI Components',
            'description': 'Star rating component for user feedback and reviews.',
            'code_snippet': '<div class="flex items-center space-x-1"><svg class="w-5 h-5 text-yellow-400 fill-current" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg><svg class="w-5 h-5 text-yellow-400 fill-current" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg><svg class="w-5 h-5 text-yellow-400 fill-current" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg><svg class="w-5 h-5 text-gray-300 fill-current" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg><svg class="w-5 h-5 text-gray-300 fill-current" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg><span class="ml-2 text-sm text-gray-600">3.0 out of 5</span></div>',
            'use_cases': 'Reviews, feedback, product ratings, user satisfaction'
        },
        {
            'component_id': 'keep_028',
            'name': 'Slider',
            'category': 'UI Components',
            'description': 'Range slider component for selecting values within a range.',
            'code_snippet': '<div class="max-w-sm"><label class="block text-sm font-medium text-gray-700 mb-2">Price Range</label><div class="relative"><input type="range" min="0" max="100" value="50" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"/><div class="flex justify-between text-xs text-gray-500 mt-1"><span>$0</span><span>$100</span></div></div></div>',
            'use_cases': 'Price filters, volume controls, range selection, settings'
        },
        {
            'component_id': 'keep_029',
            'name': 'Tab Menu',
            'category': 'UI Components',
            'description': 'Tab navigation component for organizing content into sections.',
            'code_snippet': '<div class="border-b border-gray-200"><nav class="-mb-px flex space-x-8"><button class="border-b-2 border-blue-500 text-blue-600 py-2 px-1 text-sm font-medium">Active Tab</button><button class="border-b-2 border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 py-2 px-1 text-sm font-medium">Inactive Tab</button><button class="border-b-2 border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 py-2 px-1 text-sm font-medium">Another Tab</button></nav></div>',
            'use_cases': 'Content organization, navigation, settings panels, data views'
        },
        {
            'component_id': 'keep_030',
            'name': 'Table',
            'category': 'UI Components',
            'description': 'Data table component with sorting, filtering, and pagination capabilities.',
            'code_snippet': '<div class="overflow-x-auto"><table class="min-w-full divide-y divide-gray-200"><thead class="bg-gray-50"><tr><th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th><th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Email</th><th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Role</th></tr></thead><tbody class="bg-white divide-y divide-gray-200"><tr><td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">John Doe</td><td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">john@example.com</td><td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Admin</td></tr></tbody></table></div>',
            'use_cases': 'Data display, user management, reports, content lists'
        },
        {
            'component_id': 'keep_031',
            'name': 'Text Area',
            'category': 'UI Components',
            'description': 'Multi-line text input component for longer content and comments.',
            'code_snippet': '<div class="max-w-sm"><label class="block text-sm font-medium text-gray-700 mb-2">Message</label><textarea rows="4" class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent" placeholder="Enter your message..."></textarea></div>',
            'use_cases': 'Forms, comments, descriptions, content creation'
        },
        {
            'component_id': 'keep_032',
            'name': 'Text Input',
            'category': 'UI Components',
            'description': 'Single-line text input component with validation and different states.',
            'code_snippet': '<div class="max-w-sm"><label class="block text-sm font-medium text-gray-700 mb-2">Email</label><input type="email" class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent" placeholder="Enter your email"/></div>',
            'use_cases': 'Forms, search, data entry, user input'
        },
        {
            'component_id': 'keep_033',
            'name': 'Switch Toggle',
            'category': 'UI Components',
            'description': 'Toggle switch component for binary choices and settings.',
            'code_snippet': '<div class="flex items-center space-x-3"><label class="flex items-center cursor-pointer"><input type="checkbox" class="sr-only"/><div class="relative"><div class="w-10 h-6 bg-gray-200 rounded-full shadow-inner"></div><div class="absolute w-4 h-4 bg-white rounded-full shadow top-1 left-1 transition-transform"></div></div><span class="ml-3 text-sm font-medium text-gray-700">Enable notifications</span></label></div>',
            'use_cases': 'Settings, preferences, feature toggles, binary options'
        },
        {
            'component_id': 'keep_034',
            'name': 'Tooltip',
            'category': 'UI Components',
            'description': 'Tooltip component providing additional information on hover.',
            'code_snippet': '<div class="relative group inline-block"><button class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">Hover me</button><div class="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 px-3 py-2 bg-gray-900 text-white text-sm rounded-lg opacity-0 group-hover:opacity-100 transition-opacity">This is a tooltip</div></div>',
            'use_cases': 'Help text, additional information, user guidance, context'
        },
        {
            'component_id': 'keep_035',
            'name': 'Play Button',
            'category': 'UI Components',
            'description': 'Media play button component for videos and audio content.',
            'code_snippet': '<div class="relative inline-block"><div class="w-16 h-16 bg-black bg-opacity-75 rounded-full flex items-center justify-center cursor-pointer hover:bg-opacity-90 transition"><svg class="w-8 h-8 text-white ml-1" fill="currentColor" viewBox="0 0 20 20"><path d="M8 5v10l8-5-8-5z"/></svg></div></div>',
            'use_cases': 'Video players, audio players, media controls, content preview'
        },
        {
            'component_id': 'keep_036',
            'name': 'Popover',
            'category': 'UI Components',
            'description': 'Popover component displaying contextual information or actions.',
            'code_snippet': '<div class="relative inline-block"><button class="bg-gray-200 text-gray-800 px-4 py-2 rounded-lg hover:bg-gray-300">Click me</button><div class="absolute top-full left-0 mt-2 w-64 bg-white border border-gray-200 rounded-lg shadow-lg p-4 z-10"><h3 class="font-medium text-gray-900 mb-2">Popover Title</h3><p class="text-sm text-gray-600 mb-3">This is popover content with additional information.</p><button class="text-blue-600 text-sm font-medium">Action</button></div></div>',
            'use_cases': 'Context menus, additional actions, information panels, help'
        },
        {
            'component_id': 'keep_037',
            'name': 'Search',
            'category': 'UI Components',
            'description': 'Search input component with suggestions and filtering capabilities.',
            'code_snippet': '<div class="relative max-w-sm"><div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none"><svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg></div><input type="text" class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent" placeholder="Search..."/></div>',
            'use_cases': 'Search functionality, filtering, content discovery, navigation'
        },
        {
            'component_id': 'keep_038',
            'name': 'Carousel',
            'category': 'UI Components',
            'description': 'Image carousel component with navigation controls and indicators.',
            'code_snippet': '<div class="relative max-w-lg mx-auto"><div class="overflow-hidden rounded-lg"><div class="flex transition-transform duration-300"><div class="w-full flex-shrink-0"><img src="image1.jpg" class="w-full h-64 object-cover"/></div><div class="w-full flex-shrink-0"><img src="image2.jpg" class="w-full h-64 object-cover"/></div></div></div><div class="flex justify-center space-x-2 mt-4"><button class="w-3 h-3 bg-blue-600 rounded-full"></button><button class="w-3 h-3 bg-gray-300 rounded-full"></button><button class="w-3 h-3 bg-gray-300 rounded-full"></button></div></div>',
            'use_cases': 'Image galleries, product showcases, testimonials, content rotation'
        },
        {
            'component_id': 'keep_039',
            'name': 'Tree',
            'category': 'UI Components',
            'description': 'Hierarchical tree component for displaying nested data structures.',
            'code_snippet': '<div class="space-y-1"><div class="flex items-center space-x-2"><button class="text-gray-400 hover:text-gray-600">▶</button><span class="text-sm font-medium">Parent Node</span></div><div class="ml-6 space-y-1"><div class="flex items-center space-x-2"><span class="text-gray-400">•</span><span class="text-sm text-gray-600">Child Node 1</span></div><div class="flex items-center space-x-2"><span class="text-gray-400">•</span><span class="text-sm text-gray-600">Child Node 2</span></div></div></div>',
            'use_cases': 'File browsers, navigation menus, data hierarchies, organization'
        },
        {
            'component_id': 'keep_040',
            'name': 'Toast',
            'category': 'UI Components',
            'description': 'Toast notification component for temporary messages and feedback.',
            'code_snippet': '<div class="fixed top-4 right-4 bg-white border border-gray-200 rounded-lg shadow-lg p-4 max-w-sm z-50"><div class="flex items-start"><div class="flex-shrink-0"><svg class="w-5 h-5 text-green-400" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg></div><div class="ml-3"><p class="text-sm font-medium text-gray-900">Success!</p><p class="text-sm text-gray-500">Your changes have been saved.</p></div><button class="ml-auto text-gray-400 hover:text-gray-600">×</button></div></div>',
            'use_cases': 'Notifications, feedback messages, status updates, user alerts'
        },
        {
            'component_id': 'keep_041',
            'name': 'Context Menu',
            'category': 'UI Components',
            'description': 'Right-click context menu component with action options.',
            'code_snippet': '<div class="bg-white border border-gray-200 rounded-lg shadow-lg py-1 min-w-48"><button class="w-full px-4 py-2 text-left text-sm text-gray-700 hover:bg-gray-100">Edit</button><button class="w-full px-4 py-2 text-left text-sm text-gray-700 hover:bg-gray-100">Copy</button><button class="w-full px-4 py-2 text-left text-sm text-gray-700 hover:bg-gray-100">Move</button><hr class="my-1"><button class="w-full px-4 py-2 text-left text-sm text-red-600 hover:bg-red-50">Delete</button></div>',
            'use_cases': 'Right-click menus, action menus, item operations, shortcuts'
        },
        {
            'component_id': 'keep_042',
            'name': 'Drawer',
            'category': 'UI Components',
            'description': 'Slide-out drawer component for navigation and additional content.',
            'code_snippet': '<div class="fixed inset-y-0 left-0 w-64 bg-white shadow-lg transform -translate-x-full transition-transform duration-300 ease-in-out z-50"><div class="p-6"><h3 class="text-lg font-medium text-gray-900 mb-4">Navigation</h3><nav class="space-y-2"><a href="#" class="block px-3 py-2 text-gray-700 hover:bg-gray-100 rounded-lg">Dashboard</a><a href="#" class="block px-3 py-2 text-gray-700 hover:bg-gray-100 rounded-lg">Settings</a><a href="#" class="block px-3 py-2 text-gray-700 hover:bg-gray-100 rounded-lg">Profile</a></nav></div></div>',
            'use_cases': 'Mobile navigation, sidebars, additional content, settings panels'
        },
        {
            'component_id': 'keep_043',
            'name': 'Color Picker',
            'category': 'UI Components',
            'description': 'Color selection component with palette and custom color input.',
            'code_snippet': '<div class="max-w-xs"><label class="block text-sm font-medium text-gray-700 mb-2">Choose Color</label><div class="grid grid-cols-8 gap-2"><div class="w-8 h-8 bg-red-500 rounded cursor-pointer hover:ring-2 hover:ring-gray-400"></div><div class="w-8 h-8 bg-blue-500 rounded cursor-pointer hover:ring-2 hover:ring-gray-400"></div><div class="w-8 h-8 bg-green-500 rounded cursor-pointer hover:ring-2 hover:ring-gray-400"></div><div class="w-8 h-8 bg-yellow-500 rounded cursor-pointer hover:ring-2 hover:ring-gray-400"></div><div class="w-8 h-8 bg-purple-500 rounded cursor-pointer hover:ring-2 hover:ring-gray-400"></div><div class="w-8 h-8 bg-pink-500 rounded cursor-pointer hover:ring-2 hover:ring-gray-400"></div><div class="w-8 h-8 bg-gray-500 rounded cursor-pointer hover:ring-2 hover:ring-gray-400"></div><div class="w-8 h-8 bg-black rounded cursor-pointer hover:ring-2 hover:ring-gray-400"></div></div><input type="color" class="mt-2 w-full h-10 border border-gray-300 rounded-lg"/></div>',
            'use_cases': 'Design tools, customization, theming, color selection'
        },
        {
            'component_id': 'keep_044',
            'name': 'Transfer',
            'category': 'UI Components',
            'description': 'Transfer component for moving items between two lists.',
            'code_snippet': '<div class="flex space-x-4 max-w-2xl"><div class="flex-1"><h3 class="text-sm font-medium text-gray-700 mb-2">Available Items</h3><div class="border border-gray-300 rounded-lg h-64 overflow-y-auto"><div class="p-2 hover:bg-gray-50 cursor-pointer border-b">Item 1</div><div class="p-2 hover:bg-gray-50 cursor-pointer border-b">Item 2</div><div class="p-2 hover:bg-gray-50 cursor-pointer border-b">Item 3</div></div></div><div class="flex flex-col justify-center space-y-2"><button class="px-3 py-1 text-sm bg-blue-600 text-white rounded hover:bg-blue-700">→</button><button class="px-3 py-1 text-sm bg-gray-600 text-white rounded hover:bg-gray-700">←</button></div><div class="flex-1"><h3 class="text-sm font-medium text-gray-700 mb-2">Selected Items</h3><div class="border border-gray-300 rounded-lg h-64 overflow-y-auto"><div class="p-2 hover:bg-gray-50 cursor-pointer border-b">Selected Item</div></div></div></div>',
            'use_cases': 'User management, permission assignment, data transfer, list management'
        },
        {
            'component_id': 'keep_045',
            'name': 'Light Box',
            'category': 'UI Components',
            'description': 'Lightbox component for displaying images and media in full-screen overlay.',
            'code_snippet': '<div class="fixed inset-0 bg-black bg-opacity-90 flex items-center justify-center z-50"><div class="relative max-w-4xl max-h-full p-4"><img src="large-image.jpg" class="max-w-full max-h-full object-contain"/><button class="absolute top-4 right-4 text-white text-2xl hover:text-gray-300">×</button><div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 text-white text-center"><p class="text-sm">Image Title</p><p class="text-xs text-gray-300">1 of 5</p></div></div></div>',
            'use_cases': 'Image galleries, media viewing, product showcases, content display'
        },
        {
            'component_id': 'keep_046',
            'name': 'Wysiwyg Editor',
            'category': 'UI Components',
            'description': 'Rich text editor component with formatting tools and content creation capabilities.',
            'code_snippet': '<div class="border border-gray-300 rounded-lg"><div class="border-b border-gray-300 p-2 flex space-x-2"><button class="px-3 py-1 text-sm border border-gray-300 rounded hover:bg-gray-50">B</button><button class="px-3 py-1 text-sm border border-gray-300 rounded hover:bg-gray-50">I</button><button class="px-3 py-1 text-sm border border-gray-300 rounded hover:bg-gray-50">U</button><button class="px-3 py-1 text-sm border border-gray-300 rounded hover:bg-gray-50">Link</button></div><div class="p-4 min-h-32 focus:outline-none" contenteditable="true"><p>Start typing your content here...</p></div></div>',
            'use_cases': 'Content creation, blog posts, documentation, rich text input'
        },
        {
            'component_id': 'keep_047',
            'name': 'Mega Menu',
            'category': 'UI Components',
            'description': 'Large dropdown menu component with multiple columns and rich content.',
            'code_snippet': '<div class="absolute top-full left-0 w-screen max-w-4xl bg-white border border-gray-200 rounded-lg shadow-lg z-50"><div class="grid grid-cols-3 gap-6 p-6"><div><h3 class="font-medium text-gray-900 mb-3">Products</h3><ul class="space-y-2"><li><a href="#" class="text-gray-600 hover:text-gray-900">Product 1</a></li><li><a href="#" class="text-gray-600 hover:text-gray-900">Product 2</a></li><li><a href="#" class="text-gray-600 hover:text-gray-900">Product 3</a></li></ul></div><div><h3 class="font-medium text-gray-900 mb-3">Services</h3><ul class="space-y-2"><li><a href="#" class="text-gray-600 hover:text-gray-900">Service 1</a></li><li><a href="#" class="text-gray-600 hover:text-gray-900">Service 2</a></li><li><a href="#" class="text-gray-600 hover:text-gray-900">Service 3</a></li></ul></div><div><h3 class="font-medium text-gray-900 mb-3">Resources</h3><ul class="space-y-2"><li><a href="#" class="text-gray-600 hover:text-gray-900">Resource 1</a></li><li><a href="#" class="text-gray-600 hover:text-gray-900">Resource 2</a></li><li><a href="#" class="text-gray-600 hover:text-gray-900">Resource 3</a></li></ul></div></div></div>',
            'use_cases': 'Navigation menus, product catalogs, site navigation, content organization'
        }
    ]
    
    dashboard_components = [
        {
            'component_id': 'keep_048',
            'name': 'Project Management Dashboard',
            'category': 'Dashboard',
            'description': 'Comprehensive project management dashboard with task lists, progress tracking, and team collaboration features.',
            'code_snippet': '<div class="bg-white rounded-lg shadow p-6"><div class="grid grid-cols-1 md:grid-cols-3 gap-6"><div><h3 class="text-lg font-semibold mb-4">Active Projects</h3><div class="space-y-3"><div class="p-3 border border-gray-200 rounded-lg"><h4 class="font-medium">Project Alpha</h4><div class="w-full bg-gray-200 rounded-full h-2 mt-2"><div class="bg-blue-600 h-2 rounded-full" style="width: 75%"></div></div><p class="text-sm text-gray-600 mt-1">75% Complete</p></div></div></div><div><h3 class="text-lg font-semibold mb-4">Team Members</h3><div class="space-y-2"><div class="flex items-center space-x-3"><div class="w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center text-white text-sm">JD</div><span class="text-sm">John Doe</span></div></div></div><div><h3 class="text-lg font-semibold mb-4">Recent Activity</h3><div class="space-y-2"><div class="text-sm text-gray-600">Task completed by John</div><div class="text-sm text-gray-600">New project created</div></div></div></div></div>',
            'use_cases': 'Project tracking, team management, task organization, progress monitoring'
        },
        {
            'component_id': 'keep_049',
            'name': 'Mail Application Dashboard',
            'category': 'Dashboard',
            'description': 'Email management dashboard with inbox, compose, and email organization features.',
            'code_snippet': '<div class="bg-white rounded-lg shadow h-96"><div class="flex h-full"><div class="w-1/3 border-r border-gray-200 p-4"><h3 class="font-semibold mb-3">Inbox</h3><div class="space-y-2"><div class="p-2 hover:bg-gray-50 rounded cursor-pointer border-l-4 border-blue-500"><div class="font-medium text-sm">Important Email</div><div class="text-xs text-gray-500">2 min ago</div></div><div class="p-2 hover:bg-gray-50 rounded cursor-pointer"><div class="font-medium text-sm">Newsletter</div><div class="text-xs text-gray-500">1 hour ago</div></div></div></div><div class="flex-1 p-4"><div class="h-full flex items-center justify-center text-gray-500">Select an email to view</div></div></div></div>',
            'use_cases': 'Email management, communication, inbox organization, mail clients'
        }
    ]
    
    components.extend(foundation_components)
    components.extend(ui_components)
    components.extend(additional_ui_components)
    components.extend(dashboard_components)
    
    return components


def scrape_and_save(output_path):
    """Create and save the comprehensive Keep Design component database"""
    print("Creating comprehensive Keep Design component database...")
    components = create_all_keep_design_components()
    df = pd.DataFrame(components)
    df.to_csv(output_path, index=False)
    print(f"Saved {len(df)} Keep Design components to {output_path}")
    return df


if __name__ == "__main__":
    components = create_all_keep_design_components()
    print(f"Created {len(components)} components")
    
    for i, comp in enumerate(components[:5]):
        print(f"{i+1}. {comp['name']} ({comp['category']})")