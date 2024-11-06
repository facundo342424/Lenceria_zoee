import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, TextInput, StyleSheet, Modal, TouchableOpacity } from 'react-native';
import { db } from './firebaseConfig';
import AsyncStorage from '@react-native-async-storage/async-storage';
import AntDesign from '@expo/vector-icons/AntDesign';
import SimpleLineIcons from '@expo/vector-icons/SimpleLineIcons';

const App = () => {
    const [productos, setProductos] = useState([]);
    const [nombre, setNombre] = useState('');
    const [marca, setMarca] = useState('');
    const [precio, setPrecio] = useState('');
    const [color, setColor] = useState('');
    const [modalVisible, setModalVisible] = useState(false);
    const [editModalVisible, setEditModalVisible] = useState(false);
    const [currentProductId, setCurrentProductId] = useState(null);
    const [searchText, setSearchText] = useState('');

    const fetchProductos = () => {
        db.collection('productos').onSnapshot((querySnapshot) => {
            const productosArray = [];
            querySnapshot.forEach((doc) => {
                productosArray.push({ ...doc.data(), id: doc.id });
            });
            setProductos(productosArray);
        });
    };

    useEffect(() => {
        fetchProductos();
    }, []);

    const agregarProducto = async () => {
        const nuevoProducto = { nombre, marca, precio: parseFloat(precio), color };
        await db.collection('productos').add(nuevoProducto);

        const storedProducts = JSON.parse(await AsyncStorage.getItem('productos')) || [];
        storedProducts.push(nuevoProducto);
        await AsyncStorage.setItem('productos', JSON.stringify(storedProducts));

        setNombre('');
        setMarca('');
        setPrecio('');
        setColor('');
        setModalVisible(false);
    };

    const editarProducto = () => {
        db.collection('productos').doc(currentProductId).update({
            nombre,
            marca,
            precio: parseFloat(precio),
            color,
        });

        setEditModalVisible(false);
    };

    const eliminarProducto = async (id) => {
        await db.collection('productos').doc(id).delete();
    };

    const openEditModal = (item) => {
        setCurrentProductId(item.id);
        setNombre(item.nombre);
        setMarca(item.marca);
        setPrecio(item.precio.toString());
        setColor(item.color);
        setEditModalVisible(true);
    };

    const filteredProductos = productos.filter(producto =>
        producto.nombre.toLowerCase().includes(searchText.toLowerCase())
    );

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Lista de Productos</Text>
            <TextInput
                placeholder="Buscar producto"
                value={searchText}
                onChangeText={setSearchText}
                style={styles.searchInput}
            />
            <TouchableOpacity style={styles.addButton} onPress={() => setModalVisible(true)}>
                <AntDesign name="plus" size={24} color="#fff" />
            </TouchableOpacity>

            <View style={styles.tableHeader}>
                <Text style={styles.columnHeader}>Nombre</Text>
                <Text style={styles.columnHeader}>Marca</Text>
                <Text style={styles.columnHeader}>Precio</Text>
                <Text style={styles.columnHeader}>Color</Text>
                <Text style={styles.columnHeader}>Acciones</Text>
            </View>

            <FlatList
                data={filteredProductos}
                keyExtractor={(item) => item.id}
                renderItem={({ item }) => (
                    <View style={styles.tableRow}>
                        <Text style={styles.cell}>{item.nombre}</Text>
                        <Text style={styles.cell}>{item.marca}</Text>
                        <Text style={styles.cell}>{item.precio}</Text>
                        <Text style={styles.cell}>{item.color}</Text>
                        <View style={styles.actionsContainer}>
                            <TouchableOpacity style={styles.editButton} onPress={() => openEditModal(item)}>
                                <SimpleLineIcons name="pencil" size={16} color="#fff" />
                            </TouchableOpacity>
                            <TouchableOpacity style={styles.deleteButton} onPress={() => eliminarProducto(item.id)}>
                                <AntDesign name="delete" size={16} color="#fff" />
                            </TouchableOpacity>
                        </View>
                    </View>
                )}
            />

            <Modal visible={modalVisible} transparent={true}>
                <View style={styles.modalView}>
                    <Text style={styles.modalTitle}>Agregar Producto</Text>
                    <TextInput placeholder="Nombre" value={nombre} onChangeText={setNombre} style={styles.input} />
                    <TextInput placeholder="Marca" value={marca} onChangeText={setMarca} style={styles.input} />
                    <TextInput placeholder="Precio" value={precio} onChangeText={setPrecio} keyboardType="numeric" style={styles.input} />
                    <TextInput placeholder="Color" value={color} onChangeText={setColor} style={styles.input} />
                    <TouchableOpacity style={styles.saveButton} onPress={agregarProducto}>
                        <Text style={styles.saveButtonText}>Guardar</Text>
                    </TouchableOpacity>
                    <TouchableOpacity onPress={() => setModalVisible(false)}>
                        <Text style={styles.closeButton}>Cerrar</Text>
                    </TouchableOpacity>
                </View>
            </Modal>

            <Modal visible={editModalVisible} transparent={true}>
                <View style={styles.modalView}>
                    <Text style={styles.modalTitle}>Editar Producto</Text>
                    <TextInput placeholder="Nombre" value={nombre} onChangeText={setNombre} style={styles.input} />
                    <TextInput placeholder="Marca" value={marca} onChangeText={setMarca} style={styles.input} />
                    <TextInput placeholder="Precio" value={precio} onChangeText={setPrecio} keyboardType="numeric" style={styles.input} />
                    <TextInput placeholder="Color" value={color} onChangeText={setColor} style={styles.input} />
                    <TouchableOpacity style={styles.saveButton} onPress={editarProducto}>
                        <Text style={styles.saveButtonText}>Actualizar</Text>
                    </TouchableOpacity>
                    <TouchableOpacity onPress={() => setEditModalVisible(false)}>
                        <Text style={styles.closeButton}>Cerrar</Text>
                    </TouchableOpacity>
                </View>
            </Modal>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#f8d7dab0',
        padding: 20,
    },
    title: {
        textAlign: 'center',
        marginVertical: 20,
        fontSize: 24,
        fontWeight: 'bold',
    },
    addButton: {
        backgroundColor: '#28a745',
        padding: 10,
        borderRadius: 50,
        alignItems: 'center',
        alignSelf: 'center',
        marginBottom: 10,
    },
    searchInput: {
        width: '100%',
        padding: 10,
        marginBottom: 10,
        borderWidth: 1,
        borderColor: '#ccc',
        borderRadius: 5,
    },
    tableHeader: {
        flexDirection: 'row',
        borderBottomWidth: 1,
        borderBottomColor: '#ccc',
        paddingVertical: 10,
    },
    columnHeader: {
        flex: 1,
        fontWeight: 'bold',
        textAlign: 'center',
    },
    tableRow: {
        flexDirection: 'row',
        paddingVertical: 10,
        borderBottomWidth: 1,
        borderBottomColor: '#eee',
    },
    cell: {
        flex: 1,
        textAlign: 'center',
    },
    actionsContainer: {
        flexDirection: 'row',
        justifyContent: 'space-around',
        flex: 1,
    },
    editButton: {
        backgroundColor: '#ffc107',
        padding: 5,
        borderRadius: 5,
        alignItems: 'center',
        flexDirection: 'row',
    },
    deleteButton: {
        backgroundColor: '#dc3545',
        padding: 5,
        borderRadius: 5,
        alignItems: 'center',
    },
    modalView: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: 'rgba(0, 0, 0, 0.5)',
        padding: 20,
    },
    modalTitle: {
        fontSize: 20,
        fontWeight: 'bold',
        marginBottom: 20,
    },
    input: {
        width: '100%',
        padding: 10,
        marginBottom: 10,
        borderWidth: 1,
        borderColor: '#ccc',
        borderRadius: 5,
    },
    saveButton: {
        backgroundColor: '#28a745',
        padding: 10,
        borderRadius: 5,
        alignItems: 'center',
        marginBottom: 10,
    },
    saveButtonText: {
        color: '#fff',
        fontWeight: 'bold',
    },
    closeButton: {
        color: '#fff',
        fontWeight: 'bold',
        textDecorationLine: 'underline',
    },
});

export default App;

